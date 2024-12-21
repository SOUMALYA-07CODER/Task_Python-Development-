#Alarm Clock

import datetime
import time
from playsound import playsound

alarmhr =int(input("Enter Hour: "))
alarmmin=int(input("Enter Minutes: "))
alarm = input("am / pm: ")
print("Alarm Set.....")



if alarm=="pm":
    alarmhr+=12

while True:
    if alarmhr == datetime.datetime.now().hour and alarmmin==datetime.datetime.now().minute:
        print("Time to wake up!!!")
        playsound('alarm2.mp3')

        while True:
            snooze_input = input("Do you want to snooze? (yes/no): ").strip().lower()
            snooze_duration=int(1)
            
            if snooze_input == "yes":
                print(f"Snoozing for {snooze_duration} minutes...")
                time.sleep(snooze_duration*60)
                print("wake up...wake up!!!")
                playsound('alarm2.mp3')
                
            elif snooze_input == "no":
                print("Alarm dismissed!")
                break
        break
time.sleep(1)