import os
import sys
def attempt(command):
    try:
        os.system(command)
    except KeyboardInterrupt:
        sys.exit()
try:
    attempt("java keyread.java > Dkeys.txt")
    attempt("java reader.java > Ukeys.txt")
    attempt("g++ decrypt.cpp -o dec")
    attempt("cat clear.txt > Dkeys.txt")
    attempt("./dec")
except KeyboardInterrupt:
    sys.exit()
