from jabberbot import JabberBot, botcmd
import base

class SelfPlugin(base.BasePlugin):
    @botcmd
    def uplog(self, mess, args):
        """Shows several last upwalk log messages"""
        log = self.config.get('daemon', 'log')
        return self.syscmd(["tail", "-n20", log])
