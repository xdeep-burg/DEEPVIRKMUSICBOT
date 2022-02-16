""" broadcast & statistic collector """

# Copyright (C) 2021 By adityaProject
# Originally written by aditya on github
# Broadcast function


import asyncio
import traceback
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from helpers.filters import command
from callsmusic.callsmusic import client as aditya
from config import SUDO_USERS
from helpers.decorators import sudo_users_only
from database.dbchat import get_served_chats
from database.dbusers import get_served_users
from database.dbpunish import get_gbans_count
from database.dbqueue import get_active_chats


@Client.on_message(filters.command(["acast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Stɑɤtɩŋʛ Ɓɤøɑɗƈɑst ...`")
        if not message.reply_to_message:
            await wtf.edit("**__Ƥɭɘɑsɘ Ʀɘƥɭy Ƭø ɑ Mɘssɑʛɘ Ƭø Stɑɤt Ɓɤøɑɗƈɑst ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Ɓɤøɑɗƈɑstɩŋʛ` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`gcast succesfully` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")

    


@Client.on_message(command(["bcast"]) & ~filters.edited)
@sudo_users_only
async def broadcast_message_pin(c: Client, message: Message):
    aditya = await message.reply_text("Starting ...")
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
                await aditya.edit(f"Sent To - {sent}")
            except Exception:
                pass
        await message.reply_text(
            f"✅ Broadcast complete in {sent} Group.\n📌 Sent with {pin} chat pins."
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n\n/broadcast_pin (`message`) or (`reply to message`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    aditya = await message.reply_text("Starting ...")
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            try:
                await m.pin(disable_notification=True)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
            await aditya.edit(f"Sent To - {sent}")
        except Exception:
            pass
    await message.reply_text(
        f"✅ Broadcast complete in {sent} Group.\n📌 Sent with {pin} chat pins."
    )
