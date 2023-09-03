import os
import sys
try:
    file1 = open("recmes.txt", "r")
    data = file1.read()
    if data:
        ip = file1.readline(-1).strip()
        ip = ip[24:]
        print("From " + ip + ":")
        file1.close()
    else:
        print("[!] No Data Was Received!")
        sys.exit()
except KeyboardInterrupt:
    sys.exit()
