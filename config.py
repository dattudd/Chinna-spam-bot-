#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import logging
from telethon import TelegramClient
from os import getenv
from STORM.database import DEV

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
BOT_TOKEN = getenv("BOT_TOKEN", default="7244444893:AAF6ii77hxQIVb9FCwHiqOmNjnHOngXq2c8")
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6257927828").split()))
for x in DEV:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6257927828"))
SUDO_USERS.append(OWNER_ID)
KEX1 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
KEX2 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
KEX3 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
KEX4 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
KEX5 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
KEX6 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
KEX7 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
KEX8 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
KEX9 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
KEX10 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
