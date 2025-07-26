#!/usr/bin/env python3
"""Test broadcast functionality"""

import asyncio
import aiosqlite
from config import DATABASE_PATH

async def test_broadcast_setup():
    """Test if broadcast can access users"""
    try:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute("SELECT COUNT(*) FROM users WHERE is_active IS NULL OR is_active = TRUE")
            user_count = (await cursor.fetchone())[0]
            print(f"✅ Found {user_count} active users for broadcast")
            
            # Get sample users
            cursor = await db.execute("SELECT user_id, username FROM users LIMIT 3")
            sample_users = await cursor.fetchall()
            print("📱 Sample users:")
            for user_id, username in sample_users:
                print(f"  - {user_id}: {username or 'No username'}")
                
        return True
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(test_broadcast_setup())