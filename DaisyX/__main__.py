
'''import time
import logging
import importlib
import random
import sys
import traceback
import threading
import asyncio

import pyrogram
from pyrogram import Filters
from DaisyX import daisy as app, get_self, Command

from DaisyX.modules import ALL_MODULES

StartTime = 0

loop = asyncio.get_event_loop()

async def get_runtime():
	return StartTime

async def reload_userbot():
	await app.start()
	for modul in ALL_MODULES:
		imported_module = importlib.import_module("DaisyX.modules." + modul)
		importlib.reload(imported_module)

async def reinitial_restart():
	await get_self()

async def reboot():
	global StartTime
	importlib.reload(importlib.import_module("DaisyX.modules"))
	from DaisyX.modules import ALL_MODULES
	# await setbot.send_message(Owner, "DaisyX is restarting...")
	await app.restart()
	await reinitial_restart()
	# Reset global var
	StartTime = 0
	# DaisyX userbot
	for modul in ALL_MODULES:
		imported_module = importlib.import_module("DaisyX.modules." + modul)
		if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
			imported_module.__MODULE__ = imported_module.__MODULE__
		importlib.reload(imported_module)
	# await setbot.send_message(Owner, "Restart successfully!")

async def restart_all():
	# Restarting and load all plugins
	asyncio.get_event_loop().create_task(reboot())

RANDOM_STICKERS = ["CAADAgAD6EoAAuCjggf4LTFlHEcvNAI", "CAADAgADf1AAAuCjggfqE-GQnopqyAI", "CAADAgADaV0AAuCjggfi51NV8GUiRwI"]

async def reinitial():
	await app.start()
	await get_self()
	await app.stop()

async def start_bot():
	# sys.excepthook = except_hook
	# print("----- Checking user and bot... -----")
	print("Checking DaisyX...")
	await reinitial()
	print("Check done, please wait...")
	# print("----------- Check done! ------------")
	# Assistant bot
	# DaisyX userbot
	await app.start()
	for modul in ALL_MODULES:
		imported_module = importlib.import_module("DaisyX.modules." + modul)
		if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
			imported_module.__MODULE__ = imported_module.__MODULE__
	log.info("-----------------------")
	log.info("DaisyX modules: " + str(ALL_MODULES))
	print("Module was loaded: " + ", ".join(ALL_MODULES))
	log.info("-----------------------")
	log.warning("──「 DaisyX run successfully! 」──")

if __name__ == '__main__':
	StartTime = int(time.time())
	loop.run_until_complete(start_bot())


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

'''
