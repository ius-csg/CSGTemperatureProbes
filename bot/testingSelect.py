import mysql.connector
from mysql.connector import Error


with open("../sqlinfo.txt") as f:
    sqlList = list(f.read().splitlines())
    sql_user = sqlList[0]
    sql_password = sqlList[1]   
try:
    connection = mysql.connector.connect(host="192.168.1.101",port=3306, 
                                        database='Temperature',
                                        user=sql_user,
                                        password=sql_password)

    sql_select_Query = "select * from TEMPERATURE_HISTORY"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        print("DATE = ", row[0], )
        print("DEVICE = ", row[1])
        print("TEMPERATURE = ", row[2])

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")