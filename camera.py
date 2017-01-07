from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()

subprocess.call(['aplay','sound/open_cam.wav'])

camera.start_preview()
sleep(5)
camera.capture('/home/pi/velocity_drawer/item.jpg')
camera.stop_preview()

subprocess.call(['python','identify.py','item.jpg'])
