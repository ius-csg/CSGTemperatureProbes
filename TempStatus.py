# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:38:15 2019

@author: ZAC16
"""

import pandas as pd 
import MySQLdb as db
from discord import Webhook, RequestsWebhookAdapter
    
def send_message_with_metrics(message,time,maximum, average):
    webhook = Webhook.partial(Channel_ID, 
                              Web_hook , 
                              adapter=RequestsWebhookAdapter())    
          
    webhook.send((message)% (time, maximum, average))


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
     
     # Get latest entry in the database
     
     time_of_last = p1df['ts'].iloc[[ -1]]
     
     # find highest temp and time
     time_of_max = p1df.iloc[p1df['temp'].argmax()]['ts']
     max_temp = p1df.iloc[p1df['temp'].argmax()]['temp']
     
     # get average tempurature of the week 
     week_average = (p1df['temp'].mean() + p2df['temp'].mean())/2
     
     # send status
     send_message_with_metrics("The Database is up!/n The latest entry was at %f /n The maximum record tempurature is %.2f at %f. /n The weekly average tempurature is %f.",time_of_last, time_of_max, max_temp, week_average)
     
except:
     
    webhook = Webhook.partial(Channel_ID, 
                              Web_hook , 
                              adapter=RequestsWebhookAdapter())
    
    webhook.send("@Officers Could not connect to give status.")
