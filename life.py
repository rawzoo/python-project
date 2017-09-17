#Break The Life
# #This Program is written by raju

import time 
import webbrowser

total_breaks = 3
break_count = 0
#Shows Current time of Starting of program
print("This program Starts on %s" %time.ctime())
while break_count<total_breaks:
     time.sleep(10)
     #Tells to Open a unique Adresss.....
     webbrowser.open("https://youtu.be/tt2k8PGm-TI")
     break_count = break_count + 1