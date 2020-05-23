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
from .. import loader, utils

logger = logging.getLogger(__name__)

def register(cb):
    cb(UpvoteMod())
UPVOTE = "⁪         __ \n   _    /_ |\n _| |_   | |\n|_   _|  | |\n  |_|    | |\n         |_| \n\n"
RANDOM_MESSAGE = ["I completely agree", "I strongly agree⁪", "I agree entirely", "I absolutely agree", "Point well taken!",
                 "I very much agree", "I am in full agreement", "I would have to agree with you", "I am in complete agreement",
                 "Couldn't agree more", "I wholeheartedly agree", "I quite agree with you", "I fully support this"]

class UpvoteMod(loader.Module):
    """Upvote module"""
    strings = {"name": "Upvote"}
    def __init__(self):
        self.config = loader.ModuleConfig("RANDOM_UPVOTES", RANDOM_MESSAGE, "Random upvote messages")
        
    async def upcmd(self, message):
        """.up gives an upvote"""
        upvoteMessage = random.choice(RANDOM_MESSAGE)
        await utils.answer(message,"<code>\u206a" + utils.escape_html(UPVOTE) + upvoteMessage  + "</code>")