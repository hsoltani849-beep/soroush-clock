import asyncio
import os
from datetime import datetime

from spluslib import SplusClient

SESSION_NAME = "soroush_clock"
PHONE = os.getenv("SP_PHONE")


def make_profile_name():
    time_text = datetime.now().strftime("%H:%M")

    bold_digits = str.maketrans(
        "0123456789",
        "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    )

    time_text = time_text.translate(bold_digits)

    return f"𝗣𝗥𝗫 | {time_text}"


async def main():
    if not PHONE:
        print("شماره تلفن پیدا نشد")
        return

    client = SplusClient(
        SESSION_NAME,
        device_model="Soroush Clock"
    )

    await client.start(PHONE)

    print("Soroush Clock is running...")

    last_name = None

    while True:
        profile_name = make_profile_name()

        if profile_name != last_name:
            await client.update_profile(
                first_name=profile_name,
                last_name=""
            )

            last_name = profile_name
            print("Profile updated:", profile_name)

        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
