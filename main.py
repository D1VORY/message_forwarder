from telethon import TelegramClient
import asyncio
from settings import get_client


async def main():
    client = await get_client()
    me = await client.get_me()
    print(me)

    dialogs = client.iter_dialogs()
    async for dialog in dialogs:
        print(dialog)

    client.disconnect()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
