import sys
from time import sleep
import time

def printLyrics():
    lines = [
        ("I wanna da-", 0.06), #1
        ("I wanna dance in the lights", 0.05),#2
        ("I wanna ro- ", 0.07),#3
        ("I wanna rock your body", 0.08),#4
        ("I wanna go", 0.08),#5
        ("I wanna go for a ride", 0.068),#6
        ("Hop in the music and", 0.07),#7
        ("Rock your body", 0.08),#8
        ("Rock that body",0.069),#9
        ("come on, come on", 0.035),#10
        ("Rock that body", 0.05),#11
        ("(Rock that body)", 0.03),#12
        ("Rock that body", 0.049),#13
        ("come on, come on", 0.035),#14
        ("Rock that body", 0.08),#15
    ]

allow = True
while (allow):
    v1 = int(input("enter first number: "))
    v2 = int(input("enter second number: "))   
    operation = input("enter any operation + - * / ( . to exit)")
    if (operation == "+"): print(v1+v2)
    elif (operation == "-"): print(v1-v2)
    elif (operation == "*"): print(v1*v2)
    elif (operation == "/"): print(v1/v2)
    elif (operation == "."): allow = False
    else: print("invalid option")