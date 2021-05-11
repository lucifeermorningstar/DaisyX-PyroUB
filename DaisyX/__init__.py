# (c) Copyright 21-22 by lucifeermorningstar
#
#
#
#
#

import os
import logging

from pyrogram import Client
from config import API_ID, API_HASH, STRING_SESSION, TOKEN



DaisyX = Client(
      session_name=STRING_SESSION,
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=TOKEN,
)
