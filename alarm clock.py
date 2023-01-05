import datetime 
import winsound
freq = 100
dur =50
AlarmHour=int(input("mention hour you want to wake up"))
AlarmMinute= int(input(" mention the minute want to wake up "))


AmPm=str(input("am or pm "))
if(AmPm=="pm"):
  AlarmHour=AlarmHour+12
while True:
  if(AlarmHour==datetime.datetime.now().hour 
and
AlarmMinute==datetime.datetime.now().minute):
   print("\n !!!!!WAKE UP WAKE UP!!!")
   for i in range(0, 100):
    winsound.Beep(freq, dur)
   freq= 300
   dur= 50
   break
print(" \n executed")
