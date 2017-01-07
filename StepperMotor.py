#Simply run the following commands from an appropriate location (ex. "/home/pi"):
#  git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
#  cd Adafruit-Motor-HAT-Python-Library

#Install python-dev if you havent already:
#  sudo apt-get install python-dev

#Now install it with the setup install command:
#  sudo python setup.py install


#IMPORTS
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

import json

import time
import threading
import os

#***SETUP OF MOTOR***
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr = 0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)



myStepper = mh.getStepper(200, 1)       # 200 steps/rev, motor port #1



myStepper.setSpeed(30)                  # 30 RPM

myStepper.step(400, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#***JSON***
#stepsMoved = {'position': 0}
#with open('winStat.json', 'w+') as f:
#    f.write(json.dumps(stepsMoved))

#with open('winStat.json', 'r') as f:
#    stepsMoved = json.loads(f.read())
#    print stepsMoved['position']
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#def stepper_worker(stepper, numsteps, direction, style):
#        print("Steppin!")
#        stepper.step(numsteps, direction, style)
#        print("Done")



#def spin():
#        print("Single coil steps")
#        myStepper.step(400, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

#start=spin()





# temp commands

#if stepsMoved['position'] == 0:
#	print "Window is closed all the way at the moment.\n"


#elif temp_c>15 or temp_c==15:
#		print "It's nice outside! \n Window is opening."
#		myStepper.step(400, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

#		stepsMoved = {'position': 1}
#                with open('winStat.json', 'w+') as f:
#                	f.write(json.dumps(stepsMoved))
