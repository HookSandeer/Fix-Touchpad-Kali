#!/usr/bin/python3
# By HookSander
import os
os.system("synclient tapbutton1=1")
os.system("synclient tapbutton2=3")
os.system("syndaemon -i 1 -K -t -d")
print("Enter to exit")
tmp = input()
exit()