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
# vim: ts=2:sw=2:et

import sys
import os
import logging

from upwalk.config import Configuration
from upwalk.bot import UpwalkDaemon, UpwalkJabberBot

if __name__ == "__main__":
    logging.basicConfig()
    config = Configuration()
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
