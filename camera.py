from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/smartdrawer/item.jpg')
camera.stop_preview()

subprocess.call(['python','identify.py','item.jpg'])
