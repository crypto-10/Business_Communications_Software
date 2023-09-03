import os
import time
import sys
checkerfile = 'checker.txt'
checkfile = open(checkerfile, 'r')
check = checkfile.read()
try:
    mes = input("\nEnter Message: ")
    if(mes == "!exit"):
        sys.exit()
    f = open("enter.txt", "w")
    f.write(str(mes))
    f.close()
    os.system("python3 in.py > ind.txt")                                                    #Run random indexes for KEY#2
    os.system("python3 Rand.py > output.txt")
    print("")
    print("")
    os.system("g++ Enc.cpp -o RUN")
    os.system("./RUN > keys.txt")
    os.system('cat clear.txt > ind.txt | cat clear.txt > output.txt | cat clear.txt > text.txt')        #clear the text documents used by replacing them with empty document
    os.system("java replacer.java > Fkeys.txt")
    os.system("cat clear.txt > keys.txt")
    os.system("java keyenc.java > Skeys.txt")
    #os.system("cat clear.txt > Fkeys.txt")
    os.system("python3 send.py")
    time.sleep(1)
    if("B" in check):
        os.system("sudo python3 Tran.py")
    else:
        os.system("python3 receiver.py")
    #os.system("sudo python3 Tran.py")
except KeyboardInterrupt:
    print("[!] PROGRAM TERMINATED")
    sys.exit()
