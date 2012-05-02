from jabberbot import JabberBot, botcmd
import datetime
import logging
import ConfigParser, os
from os.path import abspath, dirname, join
import sys, time
import subprocess
from daemon import Daemon

logging.basicConfig()
config = ConfigParser.ConfigParser()
config.readfp(open(join(abspath(dirname(__file__)), 'upwalk_default.conf')))
config.read(['/etc/upwalk.conf', os.path.expanduser('~/.upwalk.conf')])

class BasePlugin(JabberBot):
    def syscmd(self, args):
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        result = proc.stdout.read()
        proc.wait()
        return result


class InfoPlugin(BasePlugin):
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
 
class DiscPlugin(BasePlugin):
    @botcmd
    def df(self, mess, args):
        """Displays disc space information"""
        return self.syscmd(["df", "-h"])
    
class SelfPlugin(BasePlugin):
    @botcmd
    def uplog(self, mess, args):
        """Shows several last upwalk log messages"""
        log = config.get('daemon', 'log')
        return self.syscmd(["tail", "-n20", log])
    
class UpwalkJabberBot(SelfPlugin, InfoPlugin, DiscPlugin):
    pass
 
class UpwalkDaemon(Daemon):
    def run(self):
        jid = config.get('connection', 'jid')
        password = config.get('connection', 'password')
        resource = config.get('connection', 'resource')
        debug = config.getboolean('connection', 'debug')
        bot = UpwalkJabberBot(jid, password, resource, debug)
        bot.serve_forever()

if __name__ == "__main__":
    pid = config.get('daemon', 'pid')
    log = config.get('daemon', 'log')
    daemon = UpwalkDaemon(pid, stdout=log, stderr=log)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'foreground' == sys.argv[1]:
            daemon.run()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart|foreground" % sys.argv[0]
        sys.exit(2)
