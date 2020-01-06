# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:47:11 2019

@author: E0432298
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.runczech.com/srv/www/qf/en/ramjet/resultsEventDetail?eventId=22202&frm.subeventId=22209&page=1&per_page=15&sort=finishTime'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table', class_='resultTable font13 tableMd marginTop20 table')
# Search through the tables for the one with the headings we want.
for table in tables:
    ths = table.find_all('th')
    headings = [th.text.strip() for th in ths]
#    if headings[:11] == ['Rank in filter', 'Rank', 'Name', 'Official', 'Chip', 'St. number', 'Nationality', 'Age cat.', 'Name', 'Points', 'Compare']:
#        break
with open('runczechs.txt', 'w') as fo:
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        code_1, code_2, code_3, code_4, code_5, code_6, code_7, code_8, code_9, code_10, code_11 = [td.text.strip() for td in tds[:11]]
        # Wikipedia does something funny with country names containing
        # accented characters: extract the correct string form.
        print('; '.join([code_1, code_2, code_3, code_4, code_5, code_6, code_7, code_8, code_9, code_10, code_11]), file=fo)