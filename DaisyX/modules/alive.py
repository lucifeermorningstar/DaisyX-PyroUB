# Copyright (c) 21-22 by lucifeermorningstar@GitHub < https://github.com/lucifeermorningstar >
# Alive For DaisyX Userbot

import asyncio

from pyrogram import filters
from DaisyX import daisy

@daisy.on_message(filters.command("alive")) 
async def alive(events):
   chat = message.chat.id
   msg = await daisy.send_message(chat, "Master ! I am alive :)")
   await asyncio.sleep(2)
   await msg.edit_text(" coming soon 🔥 ") 
