import asyncio
from datetime import datetime
import os
from spluslib import SplusClient 

# تابع تبدیل اعداد به بولد یونیکد
def to_bold_numbers(text):
    normal = "0123456789"
    bold = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    trans_table = str.maketrans(normal, bold)
    return text.translate(trans_table)

async def main():
    # اطلاعات رو از تنظیمات Deplexo می‌خونیم (مرحله بعد)
    phone = os.getenv("SP_PHONE")
    
    if not phone:
        print("خطا: شماره تلفن در تنظیمات پیدا نشد!")
        return

    print("در حال اتصال به سروش...")
    client = SplusClient(phone=phone)
    
    await client.connect()
    print("اتصال موفق بود! شروع به کار ساعت...")

    last_minute = -1

    while True:
        try:
            now = datetime.now()
            current_minute = now.minute
            
            if current_minute != last_minute:
                time_str = now.strftime("%H:%M")
                new_name = f"𝗣𝗥𝗫 | {to_bold_numbers(time_str)}"
                
                await client.update_profile(name=new_name)
                print(f"ساعت به {new_name} تغییر کرد.")
                last_minute = current_minute
            
            await asyncio.sleep(30)
            
        except Exception as e:
            print(f"خطا رخ داد: {e}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
  
