import sys
import subprocess
import requests
from requests.utils import quote
import sqlite3
import cloudsight
import json

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
    pass

status = api.wait(response['token'], timeout=30)

item_name = status['name']

phrase = 'identified item, ' + item_name
subprocess.call(['pico2wave','-w','sound/identified.wav',phrase])
subprocess.call(['aplay','sound/identified.wav'])

# insert item into database
# table is called 'items', with columns item_name and location

#edit item name for location compatibility (needs space at the end)
item_name = item_name + ' '
try:
	db = sqlite3.connect('inventory.db')
	c = db.cursor()
	c.execute('INSERT INTO items (item_name,location) VALUES (?,?);',(item_name,1))
	db.commit()
except sqlite3.Error, e:
	print 'Error %s' % e.args[0]
	sys.exit(1)





