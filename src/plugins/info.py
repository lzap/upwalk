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
