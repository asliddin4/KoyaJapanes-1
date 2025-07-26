import asyncio
import sys
sys.path.append('.')

from handlers.general_content import add_general_content

async def test_upload():
    print("🧪 Testing content upload...")
    try:
        result = await add_general_content(
            section_type="speaking",
            title="Test Upload",
            description="Test description",
            content_text="Test content",
            file_type="text",
            created_by=123456789
        )
        print(f"✅ Upload test successful: {result}")
    except Exception as e:
        print(f"❌ Upload test failed: {e}")

asyncio.run(test_upload())
