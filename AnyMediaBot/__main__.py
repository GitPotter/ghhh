import os
from re import S 
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import random
from AnyMediaBot import bot as bot
from io import BytesIO
from AnyMediaBot import bot, aiohttpsession as session
from requests import get
from pyrogram.types import Message, InlineKeyboardMarkup



START_GIF = (
    "https://telegra.ph/file/a9a433ae66ae0e71da1f3.jpg",
    "https://telegra.ph/file/cf1e3d0a5063ee3110357.mp4",
)
START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(" About", callback_data="aboutmenu"),
                ],
                [
                    InlineKeyboardButton("🌺 Help 🌺", callback_data="helpmenu"),
                ],
                [
                    InlineKeyboardButton("☘️ Updates ☘️", url="https://t.me/NBOT_TEAM"),
                    InlineKeyboardButton("🌷 Support 🌷", url="https://t.me/TEAM_NBOT_GROUOP")
                ],
                [
                    InlineKeyboardButton("➕ Add me to your group ➕", url="http://t.me/EilinkMediaNTBOT?startgroup=botstart") 
                ],

            ]
        )

@bot.on_message(filters.command("start"))
async def start(bot, update):
    START_TEXT = f"""
👋 Hello {update.from_user.mention} , 🤗
🙋‍♂️ I am **[Eilink Media Bot](t.me/EilinkMediaNTBOT)**
"""
    await update.reply_photo(
                    photo=(random.choice(START_GIF)),
                    reply_markup=START_BTN,
                    caption=START_TEXT,
                    parse_mode="Html")

@bot.on_message(filters.command("help"))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=HELP_BTN)

HELP_TEXT = f"""
🙋‍♂️ I am <b>[Eilink Media Bot](t.me/EilinkMediaNTBOT)</b>
🎲 <b>Help Menu</b> 
"""
HELP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 back", callback_data="startmenu")
                ],
            ]
        )
ABOUT_TEXT = """
👋 Hello
🙋‍♂️ I am <b>[Eilink Media Bot](t.me/EilinkMediaNTBOT)</b>


"""
ABOUT_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 back", callback_data="startmenu")
                ],
            ]
        )
ST_TEXT = f"""
👋 Hello
🙋‍♂️ I am <b>[Eilink Media Bot](t.me/EilinkMediaNTBOT)</b>
"""
@bot.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(ST_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=True
    )
@bot.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELP_TEXT,
        reply_markup=HELP_BTN,
     disable_web_page_preview=True
    )
@bot.on_callback_query(filters.regex("aboutmenu"))
async def aboutenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUT_TEXT,
        reply_markup=ABOUT_BTN,
     disable_web_page_preview=True
    )

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

TEXT=f"""
☘️ **carbon Created Successfully** 
◇───────────────◇
🔥 **Created by** : @EilinkMediaNTBOT ☘️
◇───────────────◇
"""


@bot.on_message(filters.command("carbon"))
async def carbon_func(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a text message...")
    if not message.reply_to_message.text:
        return await message.reply_text("Reply to a text message...")
    m = await message.reply_text("Preparing..")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading..")
    await client.send_photo(message.chat.id, carbon,caption=TEXT)
    await m.delete()
    carbon.close()



@bot.on_message(filters.command("write"))
async def make_logo(_, message):
    imgcaption = f"""
☘️**write Successfully**
◇───────────────◇
🔥 **Created by** : @EilinkMediaNTBOT
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : [ηвσт тєαм 🇱🇰](https://t.me/NBOT_TEAM)
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text to write ✍️")
    m = await message.reply_text("✍️ writeing ..")
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app?write={text}").history[1].url
    await m.edit("📤 Uploading ...")
    await message.reply_photo(photo = photo,
                              caption=imgcaption,)
    await m.delete()

       
@bot.on_message(filters.command("logo"))
async def make_logo(_, message):
    imgcaption = f"""
☘️**LOGO Create Successfully**
◇───────────────◇
🔥 **Created by** : @EilinkMediaNTBOT
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : [ηвσт тєαм 🇱🇰](https://t.me/NBOT_TEAM)
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please provide a name... 📸")
    m = await message.reply_text(" ⭐ making Logo ...")
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logo?name={text}").history[1].url
    await m.edit("📤 Uploading ...")
    await message.reply_photo(photo = photo,
                              caption=imgcaption,)
    await m.delete() 

bot.run()
