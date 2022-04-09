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
                    InlineKeyboardButton("✨About✨", callback_data="aboutmenu"),
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
<b>👋 Hello {update.from_user.mention} , 🤗

🙋‍♂️ I am [Eilink Media Bot](t.me/EilinkMediaNTBOT)

send /help command and check my all commands 🎊🎊</b>
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
<b>🎲 Help Menu</b>

My All Commands ⇩ </b>
 ⨙●  /write  - write text  in page 😍
 ⨙●  /logo   - create logo 🧩
 ⨙●  /carbon - make carbon 🎤
 ⨙●  /help   - This Command 😅
"""
HELP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 back", callback_data="startmenu")
                ],
            ]
        )
ABOUT_TEXT = """
<b>👋 Hello

About  [Eilink Media Bot](t.me/EilinkMediaNTBOT),

✘ Name       : [Eilink Media Bot](t.me/EilinkMediaNTBOT),
✘ Create On  : [2022-04-06](t.me/NBOT_TEAM/126)
✘ Source Code:  🔐 
✘ Developer  : [ηвσт тєαм 🇱🇰](t.me/NBOT_TEAM)
✘ Thanks For : [noob #AFK](t.me/Noob_ultra_Pro_Max)

Made with ❤️ by [ηвσт тєαм 🇱🇰](t.me/NBOT_TEAM)</b>


"""
ABOUT_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 back", callback_data="startmenu")
                ],
            ]
        )
ST_TEXT = f"""
<b>👋 Hello

🙋‍♂️ I am [Eilink Media Bot](t.me/EilinkMediaNTBOT)

send /help command and check my all commands 🎊🎊</b>
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
☘️**Logo Create Successfully**
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

    
@bot.on_message(filters.command("hqlogo"))
async def make_logo(_, message):
    imgcaption = f"""
☘️**HQ Logo Create Successfully**
◇───────────────◇
🔥 **Created by** : @EilinkMediaNTBOT
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : [ηвσт тєαм 🇱🇰](https://t.me/NBOT_TEAM)
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please provide a name... 📸")
    m = await message.reply_text(" ⭐ making HQ Logo ...")
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logohq?name={text}").history[1].url
    await m.edit("📤 Uploading ...")
    await message.reply_photo(photo = photo,
                              caption=imgcaption,)
    await m.delete() 
    
    
    @asst_cmd(
    pattern="kang",
)
async def kang_cmd(ult):
    sender = await ult.get_sender()
    if not isinstance(sender, User):
        return
    if not ult.is_reply:
        return await ult.eor("`Reply to a sticker/photo..`", time=5)
    reply = await ult.get_reply_message()
    if sender.username:
        pre = sender.username[:4]
    else:
        pre = random.random_string(length=3)
    animated, dl = None, None
    try:
        emoji = ult.text.split(maxsplit=1)[1]
    except IndexError:
        emoji = None
    if reply.sticker:
        file = get_input_document(reply.sticker)
        emoji = emoji or reply.file.emoji
        if reply.file.name.endswith(".tgs"):
            animated = True
            dl = await reply.download_media()
    elif reply.photo:
        dl = await reply.download_media()
        name = "sticker.webp"
        image = TgConverter.resize_photo_sticker(dl)
        image.save(name, "WEBP")
    elif reply.text:
        dl = await Quotly().create_quotly(reply)
    else:
        return await ult.eor("`Reply to sticker or text to add it in your pack...`")
    if not emoji:
        emoji = "🏵"
    if dl:
        upl = await ult.client.upload_file(dl)
        file = get_input_document(
            await ult.client(UploadMediaRequest(InputPeerSelf(), upl))
        )
    get_ = udB.get_key("STICKERS") or {}
    type_ = "static" if not animated else "anim"
    if not get_.get(ult.sender_id) or not get_.get(ult.sender_id, {}).get(type_):
        sn = f"{pre}_{ult.sender_id}"
        title = f"{get_display_name(sender)}'s Kang Pack"
        if animated:
            type_ = "anim"
            sn += "_anim"
            title += " (Animated)"
        sn += f"_by_{asst.me.username}"
        try:
            await asst(GetSticker(InputStickerSetShortName(sn), hash=0))
            sn = sn.replace(str(ult.sender_id), f"{ult.sender_id}_{ult.id}")
        except StickersetInvalidError:
            pass
        try:
            pack = await ult.client(
                CreateStickerSetRequest(
                    user_id=sender.id,
                    title=title,
                    short_name=sn,
                    stickers=[SetItem(file, emoji=emoji)],
                    animated=animated,
                )
            )
        except Exception as er:
            return await ult.eor(str(er))
        sn = pack.set.short_name
        if not get_.get(ult.sender_id):
            get_.update({ult.sender_id: {type_: [sn]}})
        else:
            get_[ult.sender_id].update({type_: [sn]})
        udB.set_key("STICKERS", get_)
        return await ult.reply(
            f"**Kanged Successfully!\nEmoji :** {emoji}\n**Link :** [Click Here](https://t.me/addstickers/{sn})"
        )
    name = get_[ult.sender_id][type_][-1]
    try:
        await asst(GetSticker(InputStickerSetShortName(name), hash=0))
    except StickersetInvalidError:
        get_[ult.sender_id][type_].remove(name)
    try:
        await asst(
            AddSticker(InputStickerSetShortName(name), SetItem(file, emoji=emoji))
        )
    except (errors.StickerpackStickersTooMuchError, errors.StickersTooMuchError):
        sn = f"{pre}{ult.sender_id}_{ult.id}"
        title = f"{get_display_name(sender)}'s Kang Pack"
        if animated:
            sn += "_anim"
            title += " (Animated)"
        sn += f"_by_{asst.me.username}"
        try:
            pack = await ult.client(
                CreateStickerSetRequest(
                    user_id=sender.id,
                    title=title,
                    short_name=sn,
                    stickers=[SetItem(file, emoji=emoji)],
                    animated=animated,
                )
            )
        except Exception as er:
            return await ult.eor(str(er))
        get_[ult.sender_id][type_].append(pack.set.short_name)
        udB.set_key("STICKERS", get_)
        return await ult.reply(
            f"**Created New Kang Pack!\nEmoji :** {emoji}\n**Link :** [Click Here](https://t.me/addstickers/{sn})"
        )
    except Exception as er:
        LOGS.exception(er)
        return await ult.reply(str(er))
    await ult.reply(
        f"Sticker Added to Pack Successfully\n**Link :** [Click Here](https://t.me/addstickers/{name})"
    )


@asst_cmd(pattern="listpack")
async def do_magic(ult):
    ko = udB.get_key("STICKERS") or {}
    if not ko.get(ult.sender_id):
        return await ult.reply("No Sticker Pack Found!")
    al_ = []
    ul = ko[ult.sender_id]
    if ul.get("static"):
        al_.extend(ul["static"])
    if ul.get("anim"):
        al_.extend(ul["anim"])
    msg = "• **Stickers Owned by You!**\n\n"
    for _ in al_:
        try:
            pack = await ult.client(GetSticker(InputStickerSetShortName(_), hash=0))
            msg += f"• [{pack.set.title}](https://t.me/addstickers/{_})\n"
        except StickerSetInvalidError:
            if ul.get("anim") and _ in ul["anim"]:
                ul["anim"].remove(_)
            else:
                ul["static"].remove(_)
    udB.set_key("STICKERS", ko)
    await ult.reply(msg)
    
bot.run()
