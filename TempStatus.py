# # -*- coding: utf-8 -*-
# import pandas as pd 
# import MySQLdb as db
# from discord import Webhook, RequestsWebhookAdapter
# with open("sqlinfo.txt") as f:
#     sqlList = list(f.read().splitlines())
# sql_user = sqlList[0]
# sql_password = sqlList[1]   
# def send_message_with_metrics(message,time,maximum, average):
#     webhook = Webhook.partial(Channel_ID, 
#                               Web_hook , 
#                               adapter=RequestsWebhookAdapter())    
          
#     webhook.send((message)% (time, maximum, average))


# # Channel_ID = 581267637657534496
# #581253037750878264 
# Channel_ID = 538563471009120258

# # Web_hook = "lxq3T3XUspIriWj2bzNIca4m1Wdp3YfVZ10gFlR8T_OgnFo5K-NaHpWaBaTj-AMaRmFb"
# Web_hook = "NbYiMlZZWUYv0GfncYz5eh5g-5suXI535wJQsE-kJWN_sYTVBTcnOTYZuQ_pszDLrTt8"

# try:
#      conn = db.connect(host="192.168.1.101",port=3306, 
#                               user=sql_user,
#                               db="Temperature",
#                               passwd=sql_password)
     
#      query1 = "SELECT * FROM TEMPERATURE.TEMPERATURE_HISTORY WHERE ts >= DATEADD(day,-7, GETDATE()) AND DEVICE_ID = 1"
    
#      query2 = "SELECT * TEMPERATURE.TEMPERATURE_HISTORY WHERE ts >= DATEADD(day,-7, GETDATE()) AND DEVICE_ID = 2"   
     
#      p1df = pd.read_sql(query1, conn)
     
#      p2df = pd.read_sql(query2, conn)
          
#      conn.close()
     
#      # Get latest entry in the database
     
#      time_of_last = p1df['EFFDT'].iloc[[ -1]]
     
#      # find highest temp and time
#      time_of_max = p1df.iloc[p1df['temperature'].argmax()]['EFFDT']
#      max_temp = p1df.iloc[p1df['temperature'].argmax()]['temperature']
     
#      # get average tempurature of the week 
#      week_average = (p1df['temperature'].mean() + p2df['temperature'].mean())/2
     
#      # send status
#      send_message_with_metrics("The Database is up!/n The latest entry was at %f /n The maximum record temperature is %.2f at %f. /n The weekly average tempurature is %f.",time_of_last, time_of_max, max_temp, week_average)
     
# except:
     
#     webhook = Webhook.partial(Channel_ID, 
#                               Web_hook , 
#                               adapter=RequestsWebhookAdapter())
    
#     webhook.send("@Officers Could not connect to give status.")