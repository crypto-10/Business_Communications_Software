import os
def install(command, title):
    print("\033[92m\u2022 " + title + "\033[0m")
    os.system(command)
    print("\n\033[92m\u2022 Finished\n\033[0m")
install("sudo apt-get install python3", 'Installing Python3...')
install("sudo pip3 install playsound", 'Installing "playsound" package...')
