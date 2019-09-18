# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:24:52 2019

@author: ZAC16
"""
import os
import serial
import MySQLdb as db
import datetime 
with open("./sqlinfo.txt") as f:
    sqlList = list(f.read().splitlines())
    sql_user = sqlList[0]
    sql_password = sqlList[1]   
#all tempuratures will be in F
average = 0.00 # This holds the sum of the data points taken.
if os.name == 'nt':
arduinoData = serial.Serial('COM3', 9600) #Creating our serial object named arduinoData for Windows

else:
arduinoData = serial.Serial('/dev/ttyACM0', 9600) #Creating our serial object named arduinoData for NOT Windows

DataSent = True  # We do not want to send blank data to the database

try:
    conn = db.connect(host="192.168.1.101", port=3306, user=sql_user, passwd=sql_password, db="Temperature")
            
    c = conn.cursor()
    collectingData() 
    insertData()                 
    conn.commit()
    conn.close()
except Exception as e:
    
    print(e)
    
    print("Could not insert data to DB, Storing date and time...")
    
finally:
            
    average = 0.0

    cnt = 0


def collectingData():
    # while(true):
    #    go for 15 minutes
    #    break
    #do stuff to collect

def insertData():
    #insert stuff
    collectingData()

