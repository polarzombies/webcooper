#!/usr/bin/env python
'''
'''

__author__ = 'Alex Bodian'
__date__ = '04-12-2018'
__version__ = '1.0'

import io
from bs4 import BeautifulSoup
import urllib

website_url = 'http://www.nightswithalicecooper.com/on-the-air/last-nights-music/page/'

numOfplaylists = input("Enter the number of nights of music: ")
numOfplaylists = int(numOfplaylists)

