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

import logging
import requests
import json
import dateutil.parser
from datetime import datetime
from .. import loader, utils

logger = logging.getLogger(__name__)

def register(cb):
    cb(BusMod())

class BusMod(loader.Module):
    """Bus checker"""
    strings = {"name": "Bus"}
    def __init__(self):
        self.config = loader.ModuleConfig("DEFAULT_STOP", ("716"),
                                          "Enter your default stop here(numeric part only)")

    async def buscmd(self, message):
        """.bus <stop (Optional)>"""
        args = utils.get_args_raw(message)
        if not args:
            stop = "tuzsa-" + self.config["DEFAULT_STOP"]
        else:
            stop = "tuzsa-" + args
        await message.edit("<code>Procesando...</code>")
        url = "http://www.zaragoza.es/sede/servicio/urbanismo-infraestructuras/transporte-urbano/poste-autobus/" + stop + ".json"
        tries = 0
        response = requests.get(url)

        while response.status_code == 400 and tries < 10:
            response = requests.get(url)
            tries += 1
            await message.edit("<code>Intento #" + str(tries) + "...</code>")

        if response.status_code == 200:
            jsonDumps = json.dumps(response.json(), sort_keys=True)
            jsonResponse = json.loads(jsonDumps)

            try:
                lastUpdate = dateutil.parser.parse(jsonResponse['lastUpdated']).strftime("%H:%M:%S")
            except (ValueError, TypeError) as e:
                logger.error(e)
                lastUpdate = jsonResponse['lastUpdate']

            msg = jsonResponse['title'][5:].split("Líneas", 1)[0] + "\n"
            for destino in jsonResponse['destinos']:
                linea = destino['linea']
                primero = destino['primero'] if not destino['primero'].startswith('0') else "En la parada."
                segundo = destino['segundo'] if not destino['segundo'].startswith('0') else "En la parada."
                msg += "<b>• " + linea + ":</b>\n\t\t\t" + primero + "\n\t\t\t" + segundo + "\n"
            msg += "\n<i>Actualizado a la(s): " + lastUpdate + "</i>"
        elif response.status_code == 404:
            msg = "<code>Parada " + stop + " inexistente.</code>"
        else:
            msg = "<code>API caída (" + str(response.status_code) + ")</code>"
        await message.edit(msg)
