# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:48:53 2019

@author: ZAC16
"""

import serial
import os
# The serial port per machine will be different on windows it will be COM# 
# and for linux it will be /dev/ttyACM# or /dev/ttyUSB#
if os.name == 'nt':
    ser = serial.Serial('COM3', 9600)
else:
    ser = serial.Serial('/dev/ttyACM0')
serial.Serial
while True:
    if(ser.in_waiting >0):
        line = ser.readline()
        print(line)