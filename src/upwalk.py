from jabberbot import JabberBot, botcmd
import logging
import ConfigParser, os
from os.path import abspath, dirname, join
import sys
from daemon import Daemon
from plugins import *

logging.basicConfig()
config = ConfigParser.ConfigParser()
config.readfp(open(join(abspath(dirname(__file__)), 'upwalk_default.conf')))
config.read(['/etc/upwalk.conf', os.path.expanduser('~/.upwalk.conf')])

class UpwalkJabberBot(self.SelfPlugin, info.InfoPlugin, disc.DiscPlugin):
    pass
 
class UpwalkDaemon(Daemon):
    def run(self):
        jid = config.get('connection', 'jid')
        password = config.get('connection', 'password')
        resource = config.get('connection', 'resource')
        debug = config.getboolean('connection', 'debug')
        bot = UpwalkJabberBot(jid, password, resource, debug)
        bot.config = config
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
        print "usage: upwalk start|stop|restart|foreground"
        sys.exit(2)
