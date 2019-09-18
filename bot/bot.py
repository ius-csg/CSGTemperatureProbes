# bot.py
import os
import mysql.connector
from mysql.connector import Error

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!temp":
        with open("../src/sqlinfo.txt") as f:
            sqlList = list(f.read().splitlines())
            sql_user = sqlList[0]
            sql_password = sqlList[1]   
        try:
            connection = mysql.connector.connect(host="192.168.1.101",port=3306, 
                                                database='Temperature',
                                                user=sql_user,
                                                password=sql_password)

            sql_select_Query = "select * from TEMPERATURE_HISTORY T WHERE T.EFFDT = (SELECT MAX(TT.EFFDT) FROM TEMPERATURE_HISTORY TT WHERE TT.DEVICE_ID = T.DEVICE_ID)" 
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("Total number of rows in Laptop is: ", cursor.rowcount)

            print("\nPrinting each laptop record")
            embed = discord.Embed(title="Most Recent Temperature", description="CSG Lab", color=0x00ff00)
            for row in records:
                
                embed.add_field(name="DATE", value=str(row[0]), inline=True)
                embed.add_field(name="DEVICE", value=str(row[1]), inline=True)
                embed.add_field(name="TEMPERATURE", value=str(row[2]) + "\n\u200b", inline=True)
            await message.channel.send("", embed=embed)

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
client.run(TOKEN)



