#!/usr/bin/env python3
"""Simple broadcast test directly"""

import asyncio
import aiosqlite
from aiogram import Bot
from config import BOT_TOKEN, DATABASE_PATH

async def test_simple_broadcast():
    """Test simple broadcast message"""
    bot = Bot(token=BOT_TOKEN)
    
    try:
        # Get all users
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute("SELECT user_id FROM users WHERE is_active IS NULL OR is_active = TRUE")
            users = await cursor.fetchall()
        
        test_message = "🧪 Bu test xabari - admin broadcast funksiyasi ishlaydimi?"
        sent_count = 0
        
        print(f"📤 Sending to {len(users)} users...")
        
        for (user_id,) in users:
            try:
                await bot.send_message(user_id, test_message)
                sent_count += 1
                print(f"✅ Sent to {user_id}")
                await asyncio.sleep(0.1)  # Rate limit
            except Exception as e:
                print(f"❌ Failed to send to {user_id}: {e}")
        
        print(f"✅ Broadcast completed: {sent_count}/{len(users)} sent")
        
    except Exception as e:
        print(f"❌ Broadcast error: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(test_simple_broadcast())