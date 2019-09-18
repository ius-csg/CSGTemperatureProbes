# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:50:46 2019

@author: ZAC16
"""

import pandas as pd 
import MySQLdb as db
from discord import Webhook, RequestsWebhookAdapter

def send_message(message, currentTemp):
    webhook = Webhook.partial(Channel_ID, 
                              Web_hook , 
                              adapter=RequestsWebhookAdapter())
          
    highestTemp= temps1[3] if temps1[3] >= temps2[3] else temps2[3]
          
    webhook.send((message)% highestTemp)
    
def send_message_with_probe_temps(message,high, average, p1, p2):
    webhook = Webhook.partial(Channel_ID, 
                              Web_hook , 
                              adapter=RequestsWebhookAdapter())    
          
    webhook.send((message)% (high,average,p1,p2))

# Channel_ID = 581267637657534496
Channel_ID = 581253037750878264

# Web_hook = "lxq3T3XUspIriWj2bzNIca4m1Wdp3YfVZ10gFlR8T_OgnFo5K-NaHpWaBaTj-AMaRmFb"
Web_hook = "j0Lp3UhTuGoASLeU12ybCSDKyCdZJHP3DjZG5tSacCSFnVBqGNocAkwX2wJFcyRWqpGC"

try:
     conn = db.connect(host="192.168.1.249",port=3306, 
                              user="q",
                              db="Temps111A")
     
     
     query1 = "SELECT * FROM Temps111A.P1 LIMIT 4"
    
     query2 = "SELECT * FROM Temps111A.P2 LIMIT 4"   
     
     p1df = pd.read_sql(query1, conn)
     
     p2df = pd.read_sql(query2, conn)
          
     conn.close()
     
     temps1 =  p1df['P1'].to_numpy()
     
     temps2 =  p2df['P2'].to_numpy()
     
     highestTemp= temps1[3] if temps1[3] >= temps2[3] else temps2[3]
     
     averageTemp = (temps1[3]+temps2[3])/2
     
     if highestTemp >= 74:
         send_message("@everyone WARNING!!! The CSG ROOM (111A) is currently %.2f degrees fahrenheit! Send someone to turn off the Servers!!!", highestTemp)
     
     elif averageTemp >= 72:
          send_message_with_probe_temps("@Officers CAUTION!!! An area in the CSG room is reading %.2f degrees fahrenheit. \n \
The average tempurature of the room is %.2f degrees fahrenheit.\n \
Tempurature probe 1 is currently reading %.2f degrees fahrenheit. \n \
Tempuratere probe 2 is currently reading %.2f degrees fahrenheit.", highestTemp, averageTemp,temps1[3],temps2[3])
    
     
except:
     
    webhook = Webhook.partial(Channel_ID, 
                              Web_hook , 
                              adapter=RequestsWebhookAdapter())
    
    webhook.send("@Officers WARNING!!! Internal Network is down!!!")





















           
                 
                   
                    
            
            
            
            