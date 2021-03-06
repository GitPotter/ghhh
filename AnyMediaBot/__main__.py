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
                    InlineKeyboardButton("â¨Aboutâ¨", callback_data="aboutmenu"),
                ],
                [
                    InlineKeyboardButton("ðº Help ðº", callback_data="helpmenu"),
                ],
                [
                    InlineKeyboardButton("âï¸ Updates âï¸", url="https://t.me/NBOT_TEAM"),
                    InlineKeyboardButton("ð· Support ð·", url="https://t.me/TEAM_NBOT_GROUOP")
                ],
                [
                    InlineKeyboardButton("â Add me to your group â", url="http://t.me/EilinkMediaNTBOT?startgroup=botstart") 
                ],

            ]
        )

@bot.on_message(filters.command("start"))
async def start(bot, update):
    START_TEXT = f"""
<b>ð Hello {update.from_user.mention} , ð¤

ðââï¸ I am [Eilink Media Bot](t.me/EilinkMediaNTBOT)

send /help command and check my all commands ðð</b>
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
<b>ð² Help Menu</b>

My All Commands â© </b>
 â¨â  /write  - write text  in page ð
 â¨â  /logo   - create logo ð§©
 â¨â  /carbon - make carbon ð¤
 â¨â  /help   - This Command ð
 â¨â /hqlogo - create hq logo ð«
"""
HELP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ð back", callback_data="startmenu")
                ],
            ]
        )
ABOUT_TEXT = """
<b>ð Hello

About  [Eilink Media Bot](t.me/EilinkMediaNTBOT),

â Name       : [Eilink Media Bot](t.me/EilinkMediaNTBOT),
â Create On  : [2022-04-06](t.me/NBOT_TEAM/126)
â Source Code:  ð 
â Developer  : [Î·Ð²ÏÑ ÑÑÎ±Ð¼ ð±ð°](t.me/NBOT_TEAM)
â Thanks For : [noob #AFK](t.me/Noob_ultra_Pro_Max)

Made with â¤ï¸ by [Î·Ð²ÏÑ ÑÑÎ±Ð¼ ð±ð°](t.me/NBOT_TEAM)</b>


"""
ABOUT_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ð back", callback_data="startmenu")
                ],
            ]
        )
ST_TEXT = f"""
<b>ð Hello

ðââï¸ I am [Eilink Media Bot](t.me/EilinkMediaNTBOT)

send /help command and check my all commands ðð</b>
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
âï¸ **carbon Created Successfully** 
âââââââââââââââââ
ð¥ **Created by** : @EilinkMediaNTBOT âï¸
âââââââââââââââââ
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
âï¸**write Successfully**
âââââââââââââââââ
ð¥ **Created by** : @EilinkMediaNTBOT
ð· **Requestor** : {message.from_user.mention}
â¡ï¸ **Powered By **  : [Î·Ð²ÏÑ ÑÑÎ±Ð¼ ð±ð°](https://t.me/NBOT_TEAM)
âââââââââââââââââ
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text to write âï¸")
    m = await message.reply_text("âï¸ writeing ..")
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app?write={text}").history[1].url
    await m.edit("ð¤ Uploading ...")
    await message.reply_photo(photo = photo,
                              caption=imgcaption,)
    await m.delete()

       
@bot.on_message(filters.command("logo"))
async def make_logo(_, message):
    imgcaption = f"""
âï¸**Logo Create Successfully**
âââââââââââââââââ
ð¥ **Created by** : @EilinkMediaNTBOT
ð· **Requestor** : {message.from_user.mention}
â¡ï¸ **Powered By **  : [Î·Ð²ÏÑ ÑÑÎ±Ð¼ ð±ð°](https://t.me/NBOT_TEAM)
âââââââââââââââââ
"""
    if len(message.command) < 2:
            return await message.reply_text("Please provide a name... ð¸")
    m = await message.reply_text(" â­ making Logo ...")
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logo?name={text}").history[1].url
    await m.edit("ð¤ Uploading ...")
    await message.reply_photo(photo = photo,
                              caption=imgcaption,)
    await m.delete() 

    
@bot.on_message(filters.command("hqlogo"))
async def make_logo(_, message):
    imgcaption = f"""
âï¸**HQ Logo Create Successfully**
âââââââââââââââââ
ð¥ **Created by** : @EilinkMediaNTBOT
ð· **Requestor** : {message.from_user.mention}
â¡ï¸ **Powered By **  : [Î·Ð²ÏÑ ÑÑÎ±Ð¼ ð±ð°](https://t.me/NBOT_TEAM)
âââââââââââââââââ
"""
    if len(message.command) < 2:
            return await message.reply_text("Please provide a name... ð¸")
    m = await message.reply_text(" â­ making HQ Logo ...")
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logohq?name={text}").history[1].url
    await m.edit("ð¤ Uploading ...")
    await message.reply_photo(photo = photo,
                              caption=imgcaption,)
    await m.delete() 
    
@bot.on_message(filters.command("ghost"))
async def make_logo(_, message):
    imgcaption = f"""
âï¸**Ghost Logo Create Successfully**
âââââââââââââââââ
ð¥ **Created by** : @EilinkMediaNTBOT
ð· **Requestor** : {message.from_user.mention}
â¡ï¸ **Powered By **  : [Î·Ð²ÏÑ ÑÑÎ±Ð¼ ð±ð°](https://t.me/NBOT_TEAM)
âââââââââââââââââ
"""
    if len(message.command) < 2:
            return await message.reply_text("Please provide a name... ð¸")
    m = await message.reply_text(" â­ Making Ghost Logo ...")
    text = message.text.split(None, 1)[1]
    photo = get(f"https://sd-apis.up.railway.app/?logo={text}").history[1].url
    await m.edit("ð¤ Uploading ...")
    await message.reply_photo(photo = photo,
                              caption=imgcaption,)
    await m.delete()


bot.run()
