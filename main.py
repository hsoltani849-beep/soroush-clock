import asyncio
import os
from datetime import datetime

from spluslib import SplusClient


def to_bold_numbers(text):
    normal = "0123456789"
    bold = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    return text.translate(str.maketrans(normal, bold))


async def main():
    phone = os.getenv("SP_PHONE")

    if not phone:
        print("Error: Phone number not found in settings")
        return

    print("Connecting to Soroush...")

    client = SplusClient(phone)

    await client.connect()

    print("Connection successful!")

    last_name = ""

    while True:
        now = datetime.now()
        time_text = to_bold_numbers(now.strftime("%H:%M"))
        new_name = f"𝗣𝗥𝗫 | {time_text}"

        if new_name != last_name:
            await client.update_profile(
                first_name=new_name,
                last_name=""
            )

            last_name = new_name
            print("Profile updated:", new_name)

        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
