import aiohttp
import logging
from config import API_HASH, API_ID, BOT_TOKEN
from pyrogram import Client
from telethon import TelegramClient


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

bot = Client("Client", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)
tele = TelegramClient("telethon", API_ID, API_HASH)
aiohttpsession = aiohttp.ClientSession()
