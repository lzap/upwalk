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

import ConfigParser
from os.path import abspath, dirname, join, expanduser

# singleton class
class _Configuration(object):
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(join(abspath(dirname(__file__)), 'upwalk_default.conf')))
        self.config.read(['/etc/upwalk.conf', expanduser('~/.upwalk.conf')])

    def get(self, section, param):
        return self.config.get(section, param)

    def getboolean(self, section, param):
        return self.config.getboolean(section, param)

_configuration = _Configuration()
def Configuration(): return _configuration
