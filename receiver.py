import os
import subprocess
try:
    checkerfile = 'checker.txt'
    checkfile = open(checkerfile, 'r')
    check = checkfile.read()
    os.system("sudo python3 rec.py >> recmes.txt") #Bug, doesn't save, but can append
    os.system("python3 ipread.py")
    os.system("python3 Dec.py")
    os.system("cat clear.txt > recmes.txt")
    os.system("g++ playnot.cpp -o playnot")     #Note File for notifications, [!] BUG: DO NOT USE ROOT, NOT SECURE (Might cause root vulnerability) [!]
    #os.system("./playnot") #[!] DO NOT USE ROOT [!]
    #if(start.check != 1):
    if("0" in check):
        subprocess.run(["./playnot"], capture_output=True, text=True)
    if("B" in check):
        os.system("python3 receiver.py")
    else:
        os.system("sudo python3 Tran.py")
except KeyboardInterrupt:
    sys.exit()
