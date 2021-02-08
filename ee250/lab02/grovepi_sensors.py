""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""# https://github.com/usc-ee250-spring2021/lab02-AaronB19

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grovepi import *
from grove_rgb_lcd import *
from time import sleep


"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
        ultrasonic_ranger = 4
        pot = 0

        while True:
                setRGB(0,255,0) # set green as backlight color
                d = ultrasonicRead(ultrasonic_ranger)
                thresh = grovepi.analogRead(pot)
                if (d<thresh):
                        setText_norefresh(" %dcm  obj pres %dcm" %(thresh,d))
                else:
                        setText_norefresh(" %dcm           %dcm" %(thresh,d))
                sleep(0.2)

