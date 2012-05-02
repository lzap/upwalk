from jabberbot import JabberBot, botcmd
import base

class DiscPlugin(base.BasePlugin):
    @botcmd
    def df(self, mess, args):
        """Displays disc space information"""
        return self.syscmd(["df", "-h"])
