import os

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')

PHONE = os.getenv('PHONE')
USERNAME = os.getenv('USERNAME')
CHANNEL_FROM = int(os.getenv('CHANNEL_FROM'))
CHANNEL_TO = int(os.getenv('CHANNEL_TO'))

_client = None

async def get_client():
    global _client
    if not _client:
        print('IM HERE')
        client = TelegramClient(USERNAME, API_ID, API_HASH)
        await client.connect()

        # Ensure you're authorized
        if not await client.is_user_authorized():
            await client.send_code_request(PHONE)
            try:
                await client.sign_in(PHONE, input('Enter the code: '))
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Password: '))
        _client = client
        return client
    else:
        print('IM NOT HERE')
        return _client

print('FUCK YOU!')