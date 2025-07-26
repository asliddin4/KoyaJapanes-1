#!/usr/bin/env python3
"""
Fixed broadcast functionality that can be added to admin.py
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import aiosqlite
import asyncio
from aiogram import Bot
from config import BOT_TOKEN, DATABASE_PATH, ADMIN_ID
from keyboards import get_admin_menu

# States for broadcast
class BroadcastStates(StatesGroup):
    broadcast_text = State()
    broadcast_photo = State()
    broadcast_video = State() 
    broadcast_audio = State()
    broadcast_document = State()
    broadcast_caption = State()

def admin_only_check(func):
    """Simple admin check decorator"""
    from functools import wraps
    
    @wraps(func)
    async def wrapper(*args, **kwargs):
        callback_or_message = args[0] if args else None
        if not callback_or_message:
            return
            
        user_id = callback_or_message.from_user.id
        if user_id != ADMIN_ID:
            if hasattr(callback_or_message, 'answer'):
                await callback_or_message.answer("❌ Admin uchun!", show_alert=True)
            return
        return await func(*args, **kwargs)
    return wrapper

# Router for broadcast
broadcast_router = Router()

@broadcast_router.callback_query(F.data == "admin_broadcast")
@admin_only_check
async def admin_broadcast_menu(callback: CallbackQuery, state: FSMContext):
    """Broadcast menu"""
    await state.clear()
    
    if not callback.message:
        return
        
    await callback.message.edit_text(
        "📢 <b>Barchaga xabar yuborish</b>\n\n"
        "🎯 Imkoniyatlar:\n"
        "• Matn xabar\n"
        "• Rasm + matn\n"
        "• Video + matn\n"
        "• Audio + matn\n"
        "• Fayl + matn\n\n"
        "⚠️ Barcha aktiv foydalanuvchilarga yuboriladi!",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="📝 Matn", callback_data="broadcast_text"),
                InlineKeyboardButton(text="🖼 Rasm", callback_data="broadcast_photo")
            ],
            [
                InlineKeyboardButton(text="🎥 Video", callback_data="broadcast_video"),
                InlineKeyboardButton(text="🎵 Audio", callback_data="broadcast_audio")
            ],
            [
                InlineKeyboardButton(text="📎 Fayl", callback_data="broadcast_document")
            ],
            [
                InlineKeyboardButton(text="🔙 Admin panel", callback_data="admin_panel")
            ]
        ])
    )

@broadcast_router.callback_query(F.data == "broadcast_text")
@admin_only_check
async def broadcast_text_start(callback: CallbackQuery, state: FSMContext):
    """Start text broadcast"""
    await state.set_state(BroadcastStates.broadcast_text)
    
    if not callback.message:
        return
        
    await callback.message.edit_text(
        "📝 <b>Matn xabar yozish</b>\n\n"
        "Barcha foydalanuvchilarga yubormoqchi bo'lgan xabaringizni yozing:\n\n"
        "💡 HTML format ishlatishingiz mumkin\n"
        "⚠️ /cancel - bekor qilish",
        reply_markup=None
    )

@broadcast_router.message(BroadcastStates.broadcast_text)
@admin_only_check
async def broadcast_text_received(message: Message, state: FSMContext):
    """Process text message for broadcast"""
    if not message.text:
        return
        
    if message.text == "/cancel":
        await state.clear()
        await message.answer("❌ Bekor qilindi", reply_markup=get_admin_menu())
        return
    
    # Save message
    await state.update_data(message_text=message.text, message_type="text")
    
    # Show confirmation
    await message.answer(
        f"📋 <b>Tasdiqlash</b>\n\n"
        f"📝 <b>Xabar:</b>\n{message.text}\n\n"
        f"⚠️ Bu xabar barchaga yuboriladi!",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Yuborish", callback_data="confirm_broadcast"),
                InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel_broadcast")
            ]
        ])
    )

@broadcast_router.callback_query(F.data == "confirm_broadcast")
@admin_only_check
async def confirm_broadcast(callback: CallbackQuery, state: FSMContext):
    """Execute broadcast"""
    data = await state.get_data()
    
    if not data or not callback.message:
        await callback.answer("❌ Xatolik!", show_alert=True)
        return
    
    await callback.message.edit_text(
        "📤 <b>Yuborilmoqda...</b>\n\n⏳ Kuting...",
        reply_markup=None
    )
    
    # Send broadcast
    sent_count = await execute_broadcast(data)
    
    await callback.message.edit_text(
        f"✅ <b>Yuborildi!</b>\n\n"
        f"📊 Natija: {sent_count} ta foydalanuvchiga yuborildi",
        reply_markup=get_admin_menu()
    )
    
    await state.clear()

@broadcast_router.callback_query(F.data == "cancel_broadcast") 
@admin_only_check
async def cancel_broadcast(callback: CallbackQuery, state: FSMContext):
    """Cancel broadcast"""
    await state.clear()
    
    if not callback.message:
        return
        
    await callback.message.edit_text(
        "❌ <b>Bekor qilindi</b>",
        reply_markup=get_admin_menu()
    )

async def execute_broadcast(data):
    """Execute the actual broadcast"""
    bot = Bot(token=BOT_TOKEN)
    sent_count = 0
    
    try:
        # Get users
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute(
                "SELECT user_id FROM users WHERE is_active IS NULL OR is_active = TRUE"
            )
            users = await cursor.fetchall()
        
        message_type = data.get("message_type")
        message_text = data.get("message_text", "")
        
        for (user_id,) in users:
            try:
                if message_type == "text":
                    await bot.send_message(user_id, message_text)
                # Add other types later
                
                sent_count += 1
                await asyncio.sleep(0.05)  # Rate limit
                
            except Exception:
                continue  # User blocked bot
        
        return sent_count
        
    except Exception as e:
        print(f"Broadcast error: {e}")
        return sent_count
    finally:
        await bot.session.close()

if __name__ == "__main__":
    print("Fixed broadcast module ready!")