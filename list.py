import os
import sys
import subprocess
import sqlite3

db = None
item_list = None

try:
    db = sqlite3.connect('inventory.db')
    c = db.cursor()
    c.execute('SELECT item_name FROM items')
    item_list = c.fetchall()
except sqlite3.Error, e:
    print 'Error %s' % e.args[0]
	sys.exit(1) 

for item in item_list:
    print item
