# -*- coding: utf-8 -*-
"""A python interface for searching the iTunes Store"""

version_info = (1, 1, 7)
__name__ = 'itunes'
__doc__ = 'A python interface to search iTunes Store'
__author__ = ['Vinyl Darkscratch', 'Jonathan Nappi', 'Oscar Celma']
__version__ = '.'.join([str(i) for i in version_info])
__license__ = 'GPL'
__maintainer__ = 'Vinyl Darkscratch'
__email__ = ['vinyldarkscratch@gooborg.com', 'moogar@comcast.net', 'ocelma@bmat.com']
__status__ = 'Stable'

#: iTunes API version
API_VERSION = '2'

#: ISO Country Store
COUNTRY = 'US'

#: iTunes API Hostname
HOST_NAME = 'https://itunes.apple.com/'

from itunes.base import *  # NOQA
from itunes.lookup import *  # NOQA
from itunes.search import *  # NOQA
