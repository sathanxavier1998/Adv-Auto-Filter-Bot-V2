#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from bot.utils import is_subscribed

subscribed = filters.create(is_subscribed)

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private & subscribed, group=1)
async def start(bot, update):
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '💢Join Our Channel💢', url="https://t.me/Cinemaathattakam_Links"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('💥Developer💥', url='https://t.me/sathan_of_telegram'),
        InlineKeyboardButton('🔰Our Group 🔰', url ='https://t.me/cinemaathattakam_group')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/Cinemaathattakam_links')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
    
main_text = """**🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭.

Hey There Fellah, If You Need The Movie 

Click The Button Below And Join Our [CT™] Cinemaathattakam Channel.😂

Then Click The Refresh/Try Again Button And Press Start Here.🙃

You Will Get The Movie..!😁**"""
    
@Client.on_message(filters.command(["start"]) & filters.private & ~ subscribed, group=1)
async def nostart(bot, update):
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    if file_id:
        buttons = [
            [InlineKeyboardButton('Join Channel', url='https://t.me/Cinemaathattakam_Links')],
            [InlineKeyboardButton('Refresh 🔃', callback_data='refresh_btn|None')]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=update.chat.id,
            text=main_text,
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
    else:
        buttons = [
            [InlineKeyboardButton('Join Channel', url='https://t.me/Cinemaathattakam_Links')],
            [InlineKeyboardButton('Refresh 🔃', callback_data='refresh_btn|None')]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=update.chat.id,
            text=main_text,
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id
        )

@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
