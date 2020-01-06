# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:37:32 2019

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

url = "https://www.runczech.com/srv/www/qf/en/ramjet/resultsEventDetail?eventId=22202&frm.subeventId=22209&page=1&per_page=15&sort=finishTime"

url = "https://www.datacamp.com/community/tutorials"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

data = []
table = soup.find("table", { "class" : "resultTable font13 tableMd marginTop20 table" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 10:
        rank_1 = cells[1].find(text=True)
        runk_2 = cells[2].find(text=True)
        name = cells[3].find(text=True)
        off_time = cells[4].find(text=True)
        chip_time = cells[5].find(text=True)
        st_number = cells[6].find(text=True)
        national = cells[7].find(text=True)
        age = cells[7].find(text=True)
        print (rank_1)