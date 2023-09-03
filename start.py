import os
import time
import sys
events = ""
checkfilename = 'checker.txt'
def typer(pa, delay):
    for x in pa:
        time.sleep(delay)
        sys.stdout.write(x)
        sys.stdout.flush()
def writeto(path, data):
    with open(path, 'w') as sch:
        sch.write(data)
with open(checkfilename, 'r') as checker:
    contents = checker.read()
    if("X" in contents):
        writeto(checkfilename, "") #Clears Data for the checker file on start up
    else:
        pass
def appendto(path, data):
    with open(path, 'a') as sch:
        sch.write(data)
schedule = 'schedule.txt'
def printschedule():
    print("\n")
    with open(schedule, 'r') as sch:
        for line in sch:
            num = line.strip()
            print("\t\t\t\t\t" + num + "\n\t\t\t\t\t-------------------------------")
    print("\n")
def theme(col):
    os.system("clear")
    print(col + "")
    os.system("python3 start.py")
os.system("clear")
style ="""     ######
    #      #     [!] Chats are secured with end to end encryption!
   #        #
   #        #    [!] You can quit by typing "!exit"
   ##########
   ####  ####    [!] This program requires root privileges 
   ###    ###
   ##########    [!] To prevent errors, run this command: kill -9 `jobs -ps`
\n[*] Are you a sender or a receiver?
\n[0] Switch Modes
[1] Sender           <--- To send messages
[2] Receiver         <--- To receive messages
[3] Change IP or Port
[4] Enable / Disable Notifications <--- Enable/Disable Sound Notifications
[5] Help
[6] Install Modules
[7] Print IP
[8] Edit Schedule\t\t\t\t[SCHEDULE]
[9] Settings\t\t\t\t==============================
[10] Choose Theme\t\t\tEvent:    Day:       Time:"""
typer(style, 0.002)
printschedule()
try:
    ans = input("Enter Number: ")
    if ans == "1":
        os.system("sudo python3 Tran.py")
    elif ans == "2":
        os.system("python3 receiver.py")
    elif ans == "5":
        os.system("sudo python3 help.py")
    elif ans == "3":
        os.system("vim send.py")
    elif ans == "6":
        os.system("sudo python3 install.py")
    elif ans == "4":
        print("[*] Do you want to enable or disable notifications?")
        print("[1] Enable")
        print("[2] Disable")
        ans2 = input("Enter Number: ")
        if ans2 == "1":
            print("\n[*] Notifications Enabled!")
            time.sleep(3)
            writeto(checkfilename, "0")
            os.system("python3 start.py")
        elif ans2 == "2":
            print("\n[*] Notifications Disabled!")
            time.sleep(3)
            writeto(checkfilename, "1")
            os.system("python3 start.py")
        else:
            print("[!] INVALID OPTION DETECTED!")
    elif ans == "7":
        print("[!] Your IP is: ")
        os.system("hostname -I")
    elif ans == "8":
        os.system("clear")
        os.system("python3 schedule.py")
    elif ans == "0":
        print("[!] Please Make Sure to Enable or Disable Notifications Before Adjusting Modes!")
        time.sleep(2)
        print("[1] Back to Back Receive and Send Mode (Default)")
        print("[2] Receive and Send Messages")
        mode = input("\nEnter Mode Number: ")
        if (mode == "1"):
            appendto(checkfilename, "A")
            print("[!] BTB Mode ON!")
            time.sleep(2)
            os.system("python3 start.py")
        elif (mode == "2"):
            appendto(checkfilename, "B")
            print("[!] RaS Mode ON!")
            warn = "[*]RaS Mode requires two terminal windows (running this program) open, one for receiving messages and one for sending messages!"
            typer(warn, 0.01)
            time.sleep(9)
            os.system("python3 start.py")
        else:
            print("[!] INVALID OPTION SELECTED!")
    elif ans == "9":
        print("[1] Save Adjusted Settings?")
        print("[2] Reset All Settings")
        settings = input("\nEnter Number: ")
        if settings == "1":
            appendto(checkfilename, "Y")
            print("[!] Settings Saved! Do not Add or Remove any further settings!")
            time.sleep(4)
            os.system("python3 start.py")
        elif settings == "2":
            appendto(checkfilename, "X")
            print("[!] Settings Erased!")
            time.sleep(2)
            os.system("python3 start.py")
        else:
            print("[!] Invalid Option Selected!")
    elif ans == "10":
        print("[1] Red")
        print("[2] Blue")
        print("[3] Green")
        print("[4] White")
        print("[5] Yellow")
        print("[6] System")
        color = input("\nEnter Number: ")
        if color == "1":
            theme("\033[31m")
        elif color == "2":
            theme("\033[34m")
        elif color == "3":
            theme("\033[32m")
        elif color == "4":
            theme("\033[37m")
        elif color == "5":
            theme("\033[33m")
        elif color == "6":
            theme("\033[0m")
        else:
            print("[!] INVALID OPTION DETECTED!")
    elif ans == "!exit":
        sys.exit()
    else:
        print("\n[!] INVALID OPTION DETECTED!")
except KeyboardInterrupt:
    print("[!] PROGRAM TERMINATED")
    sys.exit()
