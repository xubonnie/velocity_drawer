from picamera import PiCamera
from time import sleep
import subprocess
import sqlite3

try:
    db = sqlite3.connect('inventory.db')
    c = db.cursor()    
    c.execute('SELECT * FROM items ORDER BY location ASC')
    drawer_locs = c.fetchall()
except sqlite3.Error, e:
    print 'Error %s' % e.args[0]
    sys.exit(1)

if len(drawer_locs)==5:
    subprocess.call(['aplay','sound/sorry_full.wav'])
    sys.exit(0)

camera = PiCamera()

subprocess.call(['aplay','sound/open_cam.wav'])

camera.start_preview()
sleep(5)
camera.capture('/home/pi/velocity_drawer/item.jpg')
camera.stop_preview()

subprocess.call(['python','identify.py','item.jpg'])
