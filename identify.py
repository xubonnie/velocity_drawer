import sys
import subprocess
import requests
from requests.utils import quote
import sqlite3
import cloudsight
import json

# sets up API
db = None
auth = cloudsight.SimpleAuth('E_Q05SUR2NPl-PTTOr-crg')
api = cloudsight.API(auth)

subprocess.call(['aplay','sound/please_wait.wav'])

with open('item.jpg', 'rb') as f:
    response = api.image_request(f, 'your-file.jpg', {
        'image_request[locale]': 'en-US',
    })

status = api.image_response(response['token'])
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    # Done!
    print("Shit messed up")
    pass

status = api.wait(response['token'], timeout=30)

item_name = status['name']

phrase = 'identified item, ' + item_name
subprocess.call(['pico2wave','-w','sound/identified.wav',phrase])
subprocess.call(['aplay','sound/identified.wav'])


# get items from database
try:
	db = sqlite3.connect('inventory.db')
	c = db.cursor()
	c.execute('SELECT * FROM items ORDER BY location ASC')
	drawer_locs = c.fetchall()
except sqlite3.Error, e:
	print 'Error in getting items from db %s' % e.args[0]
	sys.exit(1)

#Check if we have an empty spot
empty_spot= -1
full_spots = [i[1] for i in drawer_locs if i[0] is not 'curr_location ']
curr_location = [i[1] for i in drawer_locs if i[0] is 'curr_location '][0]
for i in range(1,5):
    if i is not in full_spots:
        empty_spot=i;
        break;

if empty_spot > 0:
    #put new item in db
    item_name = item_name + ' '
    try:
            db = sqlite3.connect('inventory.db')
            c = db.cursor()
            c.execute('INSERT INTO items (item_name,location) VALUES (?,?);',(item_name,empty_spot))
            db.commit()
    except sqlite3.Error, e:
            print 'Error from inserting new item into db %s' % e.args[0]
            sys.exit(1)
    #Spin to new spot and tell person to put in
    subprocess.call(['StepperMotor.py', curr_location, empty_spot]) 
    subprocess.call(['aplay','sound/put_item.wav'])    
else:
    #sorry we are full
    print("Sorry we are full, please take something out")
    sys.exit(0)
