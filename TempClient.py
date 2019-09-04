# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:24:52 2019

@author: ZAC16
"""

import serial
import MySQLdb as db
import datetime 

#all tempuratures will be in forinheit
average = 0.00 # This holds the sum of the data points taken.

arduinoData = serial.Serial('/dev/ttyACM0', 9600) #Creating our serial object named arduinoData

DataSent = True  # We do not want to send blank data to the database

AverageList = [] # List to store the averages, particularly if the DB goes down.

cnt = 0 # This is the number of data points taken before computing average and sent to the database.

now = datetime.datetime.now() # Get current time

print("Starting countdown to 15 mark after the hour...")

while int(now.strftime("%M")) % 15 != 0:# Do nothing until the 15 minute mark is hit
    now = datetime.datetime.now()

if(arduinoData.inWaiting()!=0):
    arduinoData.readline()

while True: # While loop that loops forever
        
    now = datetime.datetime.now() # Get current time
    
    if int(now.strftime("%M")) % 15 == 0 and DataSent is False:
        
        DataSent = True
        
        AverageList.append((datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), float(average / cnt)) )
        
        try:
            conn = db.connect(host="192.168.1.249",port=3306, 
                              user="pi#", 
                              passwd="passwd", 
                              db="Temps111A")
                 
            c = conn.cursor()
            
            # For each item in list do: insert data or insert time & data
            for item in AverageList:
                    
                     c.execute('''
                        INSERT INTO Temps111A.P# (ts,tempurature)
                        VALUES
                        (%f,%.2f)
                        ''' % (item[0],item[1]))                    
                
            AverageList.clear() # remove item put into the database
                    
            conn.commit()
                    
            print("Successfully sent data")
            
            conn.close()
        except Exception as e:
            
            print(e)
            
            print("Could not insert data to DB, Storing date and time...")
            
        finally:
                    
            average = 0.0
        
            cnt = 0
            
    elif(int(now.strftime("%M")) % 15 == 1 and DataSent is True):
        DataSent = False
        
    elif(arduinoData.inWaiting()==0):
        pass# Do Nothing
    
    else:
        arduinobyte = arduinoData.readline() #read the line of text from the serial port
        
        average += float(arduinobyte.decode('utf-8'))
        
        cnt += 1
        
        
        