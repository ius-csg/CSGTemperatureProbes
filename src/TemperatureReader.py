import os
import serial
import MySQLdb as db
import datetime 
import time

with open("./sqlinfo.txt") as f:
    sqlList = list(f.read().splitlines())
    sql_user = sqlList[0]
    sql_password = sqlList[1]   

if os.name == 'nt':
    arduinoData = serial.Serial('COM5', 9600) #Creating our serial object named arduinoData for Windows

else:
    arduinoData = serial.Serial('/dev/ttyACM0', 9600) #Creating our serial object named arduinoData for NOT Windows






def collectingData(): #this calls insert
    errorCount = 0
    average = 0
    dataSet = []
    while (errorCount < 10 and len(dataSet) < 30):
        try:
            if(arduinoData.inWaiting()!=0):	
                rawData = str(arduinoData.readline(), "utf-8")
                filteredData = rawData.strip()
                dataSet.append(float(filteredData))
                print(dataSet)
            time.sleep(1)
        except Exception as e:
            print('Data could not be read' + str(e))
            time.sleep(5)
            errorCount = errorCount+1
    average = sum(dataSet)/len(dataSet)
    print("Done! Average is %.2f" % average)
    insertData(average)

def insertData(average): #this calls collecting
    try:
        conn = db.connect(host="192.168.1.101",port=3306, 
                        user=sql_user, 
                        passwd=sql_password, 
                        db="Temperature")
        c = conn.cursor()
        if(average != 0):
            c.execute('''
            INSERT INTO Temperature.TEMPERATURE_HISTORY (EFFDT,DEVICE_ID,TEMPERATURE)
            VALUES
            (CURRENT_TIMESTAMP(),1,%.2f)
            ''' % average)                  
        conn.commit()
        print("Successfully sent data")
        conn.close()
        collectingData()
    except Exception as e:
        print(e)          

collectingData()

