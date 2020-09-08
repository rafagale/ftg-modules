# -*- coding: future_fstrings -*-

#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2020 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import random
import logging
from asyncio import sleep
from .. import loader, utils

logger = logging.getLogger(__name__)

def register(cb):
    cb(ShruggieMod())
RANDOM_MEME = ["¯\_(ツ)_/¯", "┐( ∵ )┌⁪", "¯\(◉‿◉)/¯", "¯\_ʘ‿ʘ_/¯", "¯\_༼ ಥ ‿ ಥ ༽_/¯",
                 "乁༼☯️‿☯️✿༽ㄏ", "¯\(°_o)/¯", "¯\_( ͡° ͜ʖ ͡°)_/¯", "¯¯\_༼ •́ ͜ʖ •̀ ༽_/¯",
                 "乁( •_• )ㄏ", "¯\_( ͠° ͟ʖ °͠ )_/¯", "乁( •_• )ㄏ", "¯\_(ツ)_/¯",]

class UpvoteMod(loader.Module):
    """Shruggie meme module"""
    strings = {"name": "Shruggie"}
    def __init__(self):
        self.config = loader.ModuleConfig("RANDOM_MEME", RANDOM_MEME, "Random shruggie messages")
        
    async def idkcmd(self, message):
        """.idk sends shruggies ¯\_(ツ)_/¯"""
        for x in RANDOM_MEME:
            await sleep(0.2)
            await utils.answer(message, x)
        