
import json

import sqlite3
import urllib
import ssl 

from urlparse import urljoin
from urlparse import urlparse
from BeautifulSoup import *

serviceurl = 'http://search.worldbank.org/api/v2/projects?'

conn = sqlite3.connect('project.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Profile 
    (id INTEGER PRIMARY KEY, status TEXT, project_name TEXT, url TEXT UNIQUE, sector TEXT, 
     country_name TEXT)''')

cur.execute('SELECT id,url FROM Profile WHERE status = "Active" LIMIT 1')

row = cur.fetchone()

if row is not None:
    print "Notting in BDB yet."
else :
    starturl = raw_input('Enter web url or enter: ')
    if ( len(starturl) < 1 ) : 
        starturl = 'http://search.worldbank.org/api/v2/projects?format=json&fl=id,countryname,status,project_name,sector&source=IBRD&rows=100/'
uh = urllib.urlopen(starturl)
data = uh.read ()

# print "data retreived", len(data), data

js = json.loads (data)

print json.dumps (js, indent=4)

for proj in js ['projects']:

    print 'ID', proj[('id')]
    #print 'STATUS', proj['status']
    #print 'PROJECTNAME', proj['project_name']
    #print 'URL', proj['url']
    #print 'SECTOR', proj['sector']
    #print 'COUNTRYNAME', proj['conytryname']


# cur.execute('INSERT OR IGNORE INTO Profile (id, status, project_name, url, sector, country_name) VALUES ( ?,?,?,?,?,?)''''', ( starturl, ) ) 
# conn.commit()