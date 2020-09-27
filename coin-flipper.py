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
    cb(CoinFlipperMod())
OPTIONS = ["❌", "🟤"]

class CoinFlipperMod(loader.Module):
    """Coin flipper mod"""
    strings = {"name": "CoinFlipper"}
    def __init__(self):
        self.config = loader.ModuleConfig("OPTIONS", OPTIONS, "options")
        
    async def coincmd(self, message):
        """.coin Flips a coin"""
        args = utils.get_args_raw(message)
        tries = int(3)
        if args:
            try:
                tries = int(args)
            except ValueError:
                await utils.answer(message,"<code>Error</code>")
        
        await utils.answer(message,"<code>Lanzando una moneda " + str(tries) + " veces...</code>")
        await sleep(1)

        for i in range(tries):
            i += 1
            msg = random.choice(OPTIONS)
            await sleep(1)
            await utils.answer(message,"<code>" + msg + " (#" + str(i) + ")</code>")
            if i == tries:
                await sleep(1)
                await utils.answer(message,"<code> Ha salido " + msg + " en " + str(i) + " tiradas.</code>")