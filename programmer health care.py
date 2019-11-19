print("Welcome to health care program our program is currently running")
import pygame
import datetime
a=datetime.datetime.today()
seconds = 0
minutes = 0
hours = 9
def run1(self):               ###this function for water mp3
    pygame.mixer.init()
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play()

def fun1(self):               ###this function for eye mp3
    pygame.mixer.init()
    pygame.mixer.music.load('eyes.mp3')
    pygame.mixer.music.play()

def sun1(self):                ### this function for physical mp3
    pygame.mixer.init()
    pygame.mixer.music.load('physical.mp3')
    pygame.mixer.music.play()

import time

while True:
    print(str(hours).zfill(2)+ ":" +str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 00
    if seconds == 60:
        minutes = minutes + 1
    elif seconds == 10:
        done=fun1("eyes.mp3")
        print("This is a reminder for eye exersice")
        inp=input("enter done to stop music:")
        s=pygame.mixer.music.stop()
        print(fun1)
        with open("eyes_exercise.txt","a") as f:
            f.write(f" no.1 {a} complete")
            if (inp!="done"):
                print("enter done only")
                
    elif seconds == 20:                   #### for physical exercise every 45min till 5pm
        done=fun1("physical.mp3")
        print("This is a reminder for physical exersice")
        inp=input("enter done to stop music:")
        s=pygame.mixer.music.stop()
        print(fun1)
        with open("physical_exercise.txt","a") as f:
            f.write(f" no.1 {a} complete")
            if (inp!="done"):
                print("enter done only")

        
    elif seconds == 15:                 ## drink 146ml of water every 20 minutes till 5pm
        drank=run1("water.mp3")
        print("This is a reminder to drink water")
        inp=input("enter drank to stop music:")
        s=pygame.mixer.music.stop()
        print(drank)
        with open("water_drank.txt","a") as f:
            f.write(f" no.1 {a} complete.")
            if (inp!="drank"):
                print("enter drank only")
    if minutes == 60:
        minutes = 0
        hours = hours + 1
