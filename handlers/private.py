import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/DeepVirkop-02-19",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = [DEEP VIRKâ¤ï¸](https://t.me/D33PVIRK)


ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [DEEP VIRKâ¤ï¸](https://t.me/D33PVIRK)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â â° Aá´á´ Má´ Tá´ Yá´á´Ê GÊá´á´á´ â± â", url=f"https://t.me/virkstoremusicbot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/DeepVirkop-02-19",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "D33P VIRK", url=f"https://t.me/D33PVIRK")
                ]
            ]
        ),
    )
