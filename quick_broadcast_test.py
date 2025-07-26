#!/usr/bin/env python3
"""
Quick test to verify broadcast functionality
"""

import asyncio
import aiosqlite
from aiogram import Bot
from config import BOT_TOKEN, DATABASE_PATH

async def quick_broadcast_test():
    """Send a simple test message to verify broadcast works"""
    
    bot = Bot(token=BOT_TOKEN)
    sent_count = 0
    
    try:
        print("🔍 Getting user list...")
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute("SELECT user_id, username FROM users WHERE is_active IS NULL OR is_active = TRUE LIMIT 3")
            users = await cursor.fetchall()
        
        if not users:
            print("❌ No active users found!")
            return
            
        test_message = "🧪 **Broadcast Test Message**\n\nAdmin broadcast system working correctly! ✅"
        
        print(f"📤 Sending test message to {len(users)} users...")
        
        for user_id, username in users:
            try:
                await bot.send_message(user_id, test_message)
                sent_count += 1
                print(f"✅ Sent to {user_id} (@{username or 'unknown'})")
                await asyncio.sleep(0.1)
                
            except Exception as e:
                print(f"❌ Failed to send to {user_id}: {e}")
        
        print(f"\n🎉 Test completed: {sent_count}/{len(users)} messages sent successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    print("🚀 Starting broadcast test...")
    asyncio.run(quick_broadcast_test())