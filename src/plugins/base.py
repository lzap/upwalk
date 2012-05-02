from jabberbot import JabberBot, botcmd
import subprocess

class BasePlugin(JabberBot):
    def syscmd(self, args):
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        result = proc.stdout.read()
        proc.wait()
        return result
