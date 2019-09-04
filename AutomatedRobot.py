import git 
import os
from time import sleep
currentDirectory = os.getcwd()
from datetime import datetime
now = datetime.now()
while(True):
     print("git pull from: " + currentDirectory)
     g = git.cmd.Git(currentDirectory)
     g.pull()
     sleep(60) #Dont remove this line please :D

