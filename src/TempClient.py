# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:24:52 2019

@author: ZAC16
"""
import os
import serial
import datetime 
import pandas as pd 
import MySQLdb as db

with open("./sqlinfo.txt") as f:
    sqlList = list(f.read().splitlines())
    sql_user = sqlList[0]
    sql_password = sqlList[1]   
#all tempuratures will be in Farenheit

def collectingData():
    errorCount = 0
    dataSet = []
    while errorCount < 10 and dataSet.count < 60:
        try:
            if(arduinoData.inWaiting()!=0):	
                dataSet.append(arduinoData.readline().splitlines(","))
            time.sleep(1)
        except ser.SerialTimeoutException:
            print('Data could not be read')
        time.sleep(1)
    # while(true):
    #    go for 15 minutes
    #    break
    #do stuff to collect

def insertData():
    if os.name == 'nt':
        arduinoData = serial.Serial('COM5', 9600) #Creating our serial object named arduinoData for Windows
    else:
        arduinoData = serial.Serial('/dev/ttyACM0', 9600) #Creating our serial object named arduinoData for NOT Windows

    try:
        conn = db.connect(host="192.168.1.101", port=3306, user=sql_user, passwd=sql_password, db="Temperature")
                
        c = conn.cursor()
        collectingData()                
        conn.commit()
        conn.close()
    except Exception as e:
        
        print(e)
        
        print("Could not insert data to DB, Storing date and time...")
        
    finally:
                
        average = 0.0

        cnt = 0


