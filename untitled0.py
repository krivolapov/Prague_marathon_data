# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:43:40 2019

@author: E0432298
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = "https://www.runczech.com/srv/www/qf/en/ramjet/resultsEventDetail?eventId=22202&frm.subeventId=22209&page=1&per_page=15&sort=finishTime"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')


table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
# with open('output.csv', 'wb') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerows(output_rows)