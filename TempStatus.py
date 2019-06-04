# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:38:15 2019

@author: ZAC16
"""

import pandas as pd 
import MySQLdb as db
from discord import Webhook, RequestsWebhookAdapter

def send_message(message, currentTemp):
    webhook = Webhook.partial(Channel_ID, 
                              Web_hook , 
                              adapter=RequestsWebhookAdapter())
          
    webhook.send(message)
    
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
                              user="test",
                              password="test123",
                              db="Temps111A")
     
     query1 = "SELECT * FROM Temps111A.P1 WHERE ts >= DATEADD(day,-7, GETDATE())"
    
     query2 = "SELECT * FROM Temps111A.P2 WHERE ts >= DATEADD(day,-7, GETDATE())"   
     
     p1df = pd.read_sql(query1, conn)
     
     p2df = pd.read_sql(query2, conn)
          
     conn.close()
     
     # find highest temp and time
     
     # get average of the week 
     
     # get average per day
     
     # send status
     
     
     
    
     
except:
     
    webhook = Webhook.partial(Channel_ID, 
                              Web_hook , 
                              adapter=RequestsWebhookAdapter())
    
    webhook.send("Could not connect to give status.")
