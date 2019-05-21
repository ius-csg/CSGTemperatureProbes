# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:48:53 2019

@author: ZAC16
"""

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    if(ser.in_waiting >0):
        line = ser.readline()
        print(line)