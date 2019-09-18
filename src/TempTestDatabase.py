# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:46:32 2019

@author: ZAC16
"""

import MySQLdb as db
  
try:
    conn = db.connect(host="192.168.1.249",port=3306, 
                      user="pi#", 
                      passwd="passwd", 
                      db="Temps111A")
         
    c = conn.cursor()
    
c.execute('''
      INSERT INTO Temps111A.P# (tempurature)
          VALUES
          (%.2f)
''' % (70)
            
    conn.commit()
            
    print("Successfully sent data")
    
    conn.close()
except Exception as e:
    
    print(e);
    
