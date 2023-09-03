import sys
import os
os.system("clear")
calendar = """
      ______________________
      |Su|Mo|Tu|We|Th|Fr|Sa|
X================================X
      |xx|xx|01|02|03|04|05|
      |06|07|08|09|10|11|12|      [!] Cosmetic Calendar!
      |13|14|15|16|17|18|19|
      |20|21|22|23|24|25|26|      [!] Not for actual use :)
      |27|28|29|30|31|xx|xx|
      ----------------------

"""
filepath = "schedule.txt"
print(calendar)
print("Welcome to Schedule Builder!\n============================")
print("Scheduled Events: \n----------------------------")
cont = ""
with open(filepath, 'r') as sch:
    for data in sch:
        cont = data.strip()
        print("\u2022 " + cont + "\n")
def newschedule():
    with open(filepath, 'w') as sch:  
        pass
def addtoschedule(event, day, time):
    with open(filepath, 'a') as sch:
        sch.write(event + " | " + day + " | " + time + "\n")
def deleteevent(line):
    with open(filepath, 'r') as sch:
        lines = sch.readlines()
        lines.pop(line - 1)
    with open(filepath, 'w') as sch:
        sch.writelines(lines)
def displayschedule():
    with open(filepath, 'r') as sch:
        for index, line in enumerate(sch, start=1):
            print("\n[" + str(index) + "] " + str(line.strip()) + "\n")
print("[1] Add an Event")
print("[2] Remove an Event")
print("[000] Erase All Events")
ans = input("\nEnter Number: ")
if ans == "1":
    ev = input("Enter Name of Event: ")
    if(len(ev) > 12):
        print("[!] Please Keep Event Name Less Than 12 Characters")
        sys.exit()
    da = input("Enter Day of Event(Format: D/M/Y): ")
    if(len(da) > 10 or len(da) < 8):
        print("[!] Check Your Format!")
        sys.exit()
    ti = input("Enter Time(ex: 2:30 PM): ").upper()
    if(":" not in ti):
        print("[!] INVALID TIME FORMAT")
        sys.exit()
    addtoschedule(ev,da,ti)
    print("\n[!] Event Added Succesfully!")
elif ans == "2":
    displayschedule()
    l = int(input("Which Event do You Want to Delete?\nEnter Line Number:  "))
    deleteevent(l)
    print("[!] Successfully Deleted Event at line " + str(l))
elif ans == "000":
    newschedule()
    print("[!] Schedule Cleared!")
else:
    print("[!] INVALID OPTION DETECTED!")

