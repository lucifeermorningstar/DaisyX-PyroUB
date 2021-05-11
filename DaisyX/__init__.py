# (c) Copyright 21-22 by lucifeermorningstar@GitHub, < https://GitHub.com/lucifeermorningstar >
#
# This file is part of < https://github.com/lucifeermorningstar/DaisyX-PyroUB > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/lucifeermorningstar/DaisyX-PyroUB/blob/main/LICENSE >
#
# All rights reserved.


import os
import logging

from pyrogram import Client
from config import API_ID, API_HASH, STRING_SESSION, TOKEN

StartTime = time.time()

DaisyX = Client(
      session_name=STRING_SESSION,
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=TOKEN,
      workers=3,
      sleep_threshold=5,
)

