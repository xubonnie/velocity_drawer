#takes one argument, name of item

import os
import sys
import subprocess
import time
import sqlite3


itemName = ""
db = None
loc = 0
drawer_loc = 0

for i in range(1,len(sys.argv)):
	if sys.argv[i] == 'Penn':
		itemName = itemName + 'pen '
	else:
		itemName = itemName + sys.argv[i] + ' '

#search for item in database
#database is called 'items', with columns item_name and location
try:
	db = sqlite3.connect('inventory.db')
	c = db.cursor()
	c.execute('SELECT location FROM items WHERE item_name=:item',{"item": itemName})
	loc = c.fetchone()
	print loc
	c.execute('SELECT location FROM items WHERE item_name="location ";')
	drawer_loc = c.fethone()

except sqlite3.Error, e:
	print 'Error %s' % e.args[0]
	sys.exit(1)


found = False

if (not(loc == None)):
	loc = loc[0]
	drawer_loc = drawer_loc[0]
	itemName = itemName + 'located in, slot ' + str(loc)
	subprocess.call(['pico2wave', '-w', 'sound/located.wav', itemName])
	subprocess.call(['aplay', 'sound/located.wav'])
	#update database to reflect new location
	try:
                c.execute('UPDATE items SET location=(?) WHERE item_name="curr_location ";',(loc))
        except sqlite3.Error, e:
                print 'Error %s' % e.args[0]

	#delay
	subprocess.call(['python','StepperMotor.py',drawer_loc,loc])
	#update database to reflect new location
	#try:
	#	c.execute('UPDATE items SET location=(?) WHERE item_name="curr_location ";',(loc))
	#except sqlite3.Error, e:
	#	print 'Error %s' % e.args[0]
else:
	itemName = 'unable to locate, ' + itemName
	subprocess.call(['pico2wave', '-w', 'sound/unabletolocate.wav', itemName])
	subprocess.call(['aplay', 'sound/unabletolocate.wav'])
