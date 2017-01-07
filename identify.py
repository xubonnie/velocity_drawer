import sys
import subprocess
import requests
from requests.utils import quote
import sqlite3

db = None

subprocess.call(['aplay','sound/please_wait.wav'])

URL = "https://visual-recognition-demo.mybluemix.net/api/classify"
img_name = sys.argv[1]
files = {'images_file':open(img_name,'rb')} #modes r and b are for read and binary
r = requests.post(URL, files=files)

find_string = ':"'
start = r.text.find(find_string) + len(find_string)
item_name = r.text[start:(r.text.find('"',start))]
#print(r.text)
#print(item_name)

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
