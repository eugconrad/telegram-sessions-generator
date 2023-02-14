#
#     d88P     d88P          888b    888          888
#      d88P   d88P           8888b   888          888
#       d88P d88P            88888b  888          888
#        d88888P    888888   888Y88b 888  .d88b.  888888
#        d88888P    888888   888 Y88b888 d8P  Y8b 888
#       d88P d88P            888  Y88888 88888888 888
#      d88P   d88P           888   Y8888 Y8b.     Y88b.
#     d88P     d88P          88.8    Y888  "Y8888   "Y888
#
#                      © Copyright 2022
#                    https://x-net.pp.ua
#                 https://github.com/Conradk10
#
#                 Licensed under the GNU GPLv3
#          https://www.gnu.org/licenses/agpl-3.0.html
#

import asyncio
import os

from loguru import logger
from telethon.sync import TelegramClient

from config import (
    API_ID,
    API_HASH,
    DEVICE_MODEL,
    SYSTEM_VERSION,
    APP_VERSION,
    LANG_CODE,
    SYSTEM_LANG_CODE,
    SESSIONS_DIR,
)
from utils import get_sessions_list


async def main():
    while True:
        sessions = get_sessions_list()
        logger.info(f"Сессии: {sessions}")
        session = input("Введите название сессии (латиницей, без пробелов и специальных символов): ")
        if sessions and f"{SESSIONS_DIR}/{session}.session" in sessions:
            logger.error(f"Сессия с именем {session} уже существует!")
            answer = input(f"Пересоздать сессию с именем {session}? [Да/Нет]")
            if answer.lower() in ["y", "yes", "да", "д"]:
                os.remove(f"{SESSIONS_DIR}/{session}.session")
                await asyncio.sleep(.5)
            else:
                continue
        client = TelegramClient(
            session=f"{SESSIONS_DIR}/{session}.session",
            api_id=API_ID,
            api_hash=API_HASH,
            device_model=DEVICE_MODEL,
            system_version=SYSTEM_VERSION,
            app_version=APP_VERSION,
            lang_code=LANG_CODE,
            system_lang_code=SYSTEM_LANG_CODE
        )
        await client.start()
        await client.disconnect()
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
