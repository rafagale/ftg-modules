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
    cb(RektMod())
REKTS = ["Not rekt", "Rekt⁪", "Really Rekt", "Tyrannosaurus Rekt", "Parks and Rekt",
                 "Star Trekt", "School Of Rekt", "Catcher in the Rekt", "Great Rektspectations",
                 "Rekt It Ralph", "www.rekkit.com", "The Shawshank Rektemption", "Forrekt Gump",
                 "Finding Rekt", "Shrekt", "Rektal Exam", "Rektium for a Dream", "Erektile Dysfunction"]
UNTICK = "☐ "
TICK  = "☑ "

class RektMod(loader.Module):
    """RektMod meme module"""
    strings = {"name": "Rekt"}
    def __init__(self):
        self.config = loader.ModuleConfig("REKTS", REKTS, "Random rekts messages")
        
    async def rektcmd(self, message):
        """.rekt sends rekts"""
        msg = ""
        for x in REKTS:
            await sleep(0.4)
            if "Not rekt" in x:
                msg += UNTICK
            else:
                msg += TICK
            msg += x + "\n"
            await message.edit(msg)