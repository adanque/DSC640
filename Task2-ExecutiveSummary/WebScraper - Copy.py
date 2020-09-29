# Name: Alan Danque
# Date: 20200918
# Course: DSC 640
# Desc:
# Scrapes  Information from the  web site
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.baaa-acro.com/crash-archives?created=&created_1=&field_crash_region_target_id=All&field_crash_country_target_id&field_crash_registration_target_id&field_crash_aircraft_target_id&field_crash_operator_target_id&field_crash_cause_target_id=All&field_crash_zone_target_id&field_crash_site_type_target_id=All&field_crash_phase_type_target_id=All&field_crash_flight_type_target_id=All&field_crash_survivors_value=All&field_crash_city_target_id&page=1"
r = requests.get(URL)

#soup = BeautifulSoup(r.content, 'html5lib')
soup = BeautifulSoup(r.content, "lxml")

table = soup.find('thead')
tr0 = table.findAll('tr')

# Get the Column Headers
for row in tr0:
    col1 = row.findAll('th')
    header = (
     str(col1[0].get_text())
    ,str(col1[1].get_text())
    ,str(col1[2].get_text())
    ,str(col1[3].get_text())
    ,str(col1[4].get_text())
    ,str(col1[5].get_text())
    ,str(col1[6].get_text())
    ,"URL"
#    ,str(col1[7].get_text())
    )


tabletop = tuple(header)
table = soup.find('tbody')
tr1 = table.findAll('tr')

detail = []
for row in tr1:
    new_row = {}
    col1 = row.findAll('td')
    col2 = row.findAll('a')
    detail_row = (
        str(col1[0].get_text())
        , str(col1[1].get_text())
        , str(col1[2].get_text())
        , str(col1[3].get_text())
        , str(col1[4].get_text())
        , str(col1[5].get_text())
        , str(col1[6].get_text())
        , str(col2[0].get('href'))
#        , datetime.today().date()
#        , datetime.today().strftime('%H:%M')  # datetime.strptime(todaydt, '%H:%M:%S.%f')   #datetime.today().time()
#        , datetime.today().weekday()
#        , str(col1[9].get_text()).replace("%", "")
        )
    new_row = dict(zip(tabletop, detail_row))
    detail.append(new_row)





filename = '.\\datasets\\AviationDataSupplement_baaa-acro.csv'
with open(filename, 'w', newline='', encoding="utf-8") as f:
    w = csv.DictWriter(f, ['Image', 'Date', 'Operator', 'A/C Type', 'Location', 'Fatalities', 'Registration', 'URL'])
    w.writeheader()
    for detailrow in detail:
        w.writerow(detailrow)

