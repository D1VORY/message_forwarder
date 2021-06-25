from telethon import TelegramClient, events
from telethon.errors import MessageIdInvalidError
from telethon.events import NewMessage
import asyncio
from settings import get_client, CHANNEL_FROM, CHANNEL_TO

client = asyncio.get_event_loop().run_until_complete(get_client())


@client.on(events.NewMessage(chats=[CHANNEL_FROM]))
async def my_event_handler(event: NewMessage):
    try:
        await client.forward_messages(CHANNEL_TO, event.message)
    except MessageIdInvalidError:
        pass

async def fuck():
    dialogs = client.iter_dialogs()
    async for dialog in dialogs:
        print(dialog)


client.start()
#client.loop.run_until_complete(fuck())
client.run_until_disconnected()
