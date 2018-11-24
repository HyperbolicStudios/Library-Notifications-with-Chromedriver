#Calendar Modules
from __future__ import print_function
from apiclient import discovery
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#Selenium Modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#os Modules
import os
from inspect import getsourcefile
from os.path import abspath

#General Modules
import time
import datetime

#Find the curent file location/chdir to current location
directory = abspath(getsourcefile(lambda:0))
newDirectory = directory[:(directory.rfind("\\")+1)]
os.chdir(newDirectory)


#Calendar API Setup

def calendar (date, title):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

    GMT_OFF = '-07:00'      # PDT/MST/GMT-7

    EVENT = {
        title: 'GVPL Item Due',
        'start':  {'dateTime': date+'T06:00:00%s' % GMT_OFF},
        'end':    {'dateTime': date+'T06:30:00%s' % GMT_OFF},

    }

    e = GCAL.events().insert(calendarId='primary',
            sendNotifications=True, body=EVENT).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (e['summary'].encode('utf-8'),
            e['start']['dateTime'], e['end']['dateTime']))
    return;




#-----------------------------------------



i =1;

ID_A = "j_username"
ID_B = "j_password"
username = "369135m"
password = "MashedPotatoes"

options = Options()
options.add_argument('--headless')

PATH = ("C:\\Users\\marki\\Documents\\chromedriver.exe")


driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
time.sleep(1)
driver.get("""https://gvpl.ent.sirsidynix.net/client/en_US/default/
search/patronlogin/https:$002f$002fgvpl.ent.sirsidynix.net$002fclient$002fen_US$002fdefault$002fsearch$002faccount$003f/"""
)
print("!!!!!!!!!!!!!!!!")

time.sleep(2)
driver.find_element_by_id(ID_A).send_keys(username)
driver.find_element_by_id(ID_B).send_keys(password)
driver.find_element_by_id("submit_0").click()

#User Page
time.sleep(2)
driver.find_element_by_link_text("Checkouts").click()
el=(driver.find_element_by_css_selector("html"))

text = el.text

x = text.find("Total Items Checked Out:")
x = (text[(x+25):(x+27)])
x = int(x) + 1
while i < x:
    argument = "//table[@id='myCheckouts_checkoutslist_table']/tbody/tr[@class='checkoutsLine'][" + (str(i)) + "]"
    el=(driver.find_element_by_xpath(argument))
    print("-----------------------------")
    text = (el.text)

    #-------------------------

    length = len(text)
    date = text[(length-9):length]

    length = len(date)

    year = "20" + (date[(length-2):length])
    year = int(year)

    date = (date[:(length-3)])

    location = date.find("/")

    day = int(date[(location+1):(location+3)])
    month = int(date[(location-2):(location)])




    d0 = datetime.date(year, month, day)
    d1 = datetime.date.today()
    delta = d0 - d1
    countdown = (delta.days)

    dateTomorrow = d1 + datetime.timedelta(days=1)
    dateTomorrow = str(dateTomorrow)

    value = (text.splitlines()[3])
    title = (text.splitlines()[0])
    value = value + " | " + str(d0)

    file = open('itemlogs.txt', 'r')
    logs = file.read()
    results = logs.count(value)
    file.close()

    print("----------------------------------------")
    #add to calendar or onenote, if due in 2 days AND not already logged
    if (countdown < 3 and results == 0):
        print("Logging. Search result: " + str(results))
        file = open('itemlogs.txt', 'a')
        file.write(value + "\n")
        file.close()
        value = "Added to calendar."

        calendar(dateTomorrow, title)
   else:
       value = "Did not add to calendar."


    print(text)
    print("Due in: " + str(countdown) + " days.")
    print(value)

    i = i+1


driver.quit()
