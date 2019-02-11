from bs4 import BeautifulSoup
import urllib.request
import csv
from datetime import datetime
import re

quote_page = {'http://scholarships.studentscholarships.org/',
            'http://www.hec.gov.pk/english/scholarshipsgrants/Pages/NationalScholarships.aspx',
              'http://www.scholars4dev.com/'}
for link in quote_page:
    page = urllib.request.urlopen(link).read().decode('utf-8')
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        name = link.get('href')
        print(name)
        title = link.string
        print(title)
        with open('links.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([title,name])


   
