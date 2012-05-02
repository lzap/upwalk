# vim: ts=4:sw=4:et
#
# Copyright 2012 Lukas Zapletal and other authors
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

import sys
import os

from jabberbot import JabberBot, botcmd

from daemon import Daemon
from config import Configuration
from plugins import *

class UpwalkJabberBot(self.SelfPlugin, info.InfoPlugin, disc.DiscPlugin):
    pass

class UpwalkDaemon(Daemon):
    def run(self):
        config = Configuration()
        jid = config.get('connection', 'jid')
        password = config.get('connection', 'password')
        resource = config.get('connection', 'resource')
        debug = config.getboolean('connection', 'debug')
        bot = UpwalkJabberBot(jid, password, resource, debug)
        bot.serve_forever()
