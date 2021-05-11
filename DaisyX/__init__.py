# (c) Copyright 21-22 by lucifeermorningstar@GitHub, < https://GitHub.com/lucifeermorningstar >
#
# This file is part of < https://github.com/lucifeermorningstar/DaisyX-PyroUB > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/lucifeermorningstar/DaisyX-PyroUB/blob/main/LICENSE >
#
# All rights reserved.


import os
import time
import logging

from pyrogram import Client
from config import API_ID, API_HASH, STRING_SESSION, TOKEN


StartTime = time.time()

daisy = Client(
      session_name=STRING_SESSION,
      api_id=API_ID,
      api_hash=API_HASH,
      sleep_threshold=180,
)

assist = Client(
        "MyAssistant",
        api_id=API_ID,
        api_hash= API_HASH,
        bot_token=TOKEN,
        sleep_threshold=180,
    )


''' For Skem Purpose

Owner = 0
OwnerName = ""
OwnerUsername = ""

TEST_DEVELOP = False
	
async def get_self():
	global Owner, OwnerName, OwnerUsername

	getself = await daisy.get_me()
	Owner = getself.id
	if getself.last_name:
		OwnerName = getself.first_name + " " + getself.last_name
	else:
		OwnerName = getself.first_name
	OwnerUsername = getself.username
	if not TEST_DEVELOP:
		print("Welcome: {}".format(OwnerName))

# Command Prefix
Command = [".", "!","?"]'''


# By Lodu Swonit

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    return [
        basename(f)[:-3] for f in mod_paths if isfile(f)
        and f.endswith(".py")
        and not f.endswith('__init__.py')
        ]


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
