from jabberbot import JabberBot, botcmd
import datetime
import logging
import ConfigParser, os
from os.path import abspath, dirname, join
import sys, time
from daemon import Daemon

logging.basicConfig()
config = ConfigParser.ConfigParser()
config.readfp(open(join(abspath(dirname(__file__)), 'upwalk_default.conf')))
config.read(['/etc/upwalk.conf', os.path.expanduser('~/.upwalk.conf')])

class SystemInfoJabberBot(JabberBot):
    @botcmd
    def serverinfo( self, mess, args):
        """Displays information about the server"""
        version = open('/proc/version').read().strip()
        loadavg = open('/proc/loadavg').read().strip()

        return '%s\n\n%s' % ( version, loadavg, )
    
    @botcmd
    def time( self, mess, args):
        """Displays current server time"""
        return str(datetime.datetime.now())

    @botcmd
    def rot13( self, mess, args):
        """Returns passed arguments rot13'ed"""
        return args.encode('rot13')

    @botcmd
    def whoami(self, mess, args):
        """Tells you your username"""
        return mess.getFrom().getStripped()
 
class UpwalkDaemon(Daemon):
    def run(self):
        jid = config.get('connection', 'jid')
        password = config.get('connection', 'password')
        resource = config.get('connection', 'resource')
        debug = config.getboolean('connection', 'debug')
        bot = SystemInfoJabberBot(jid, password, resource, debug)
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
