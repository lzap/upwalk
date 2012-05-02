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

from jabberbot import JabberBot, botcmd
import base
import datetime

class InfoPlugin(base.BasePlugin):
    @botcmd
    def uname(self, mess, args):
        """Displays uname information"""
        return open('/proc/version').read().strip()
    
    @botcmd
    def uptime(self, mess, args):
        """Displays uptime information"""
        return self.syscmd(["uptime"])
    
    @botcmd
    def load(self, mess, args):
        """Displays load information"""
        return open('/proc/loadavg').read().strip()
    
    @botcmd
    def time( self, mess, args):
        """Displays current server time"""
        return str(datetime.datetime.now())

    @botcmd
    def whoami(self, mess, args):
        """Tells you your username"""
        return mess.getFrom().getStripped()
