import time
import sys
def out(chars):
    print(chars)
    time.sleep(0.15)
try:
    out('\033[31m\n########                #    #######                                               #        ######')
    out('   #                    #    #                                                     #       #      #')
    out('   #           #        #    #                                                   #####    #        #')
    out('   #      ###      ######    ######    ####     ####    ###   #    #   ######      #      #        #')
    out('   #     #     #  #     #    #         #   #   #        #      #  #    #    #      #      ##########')
    out('\033[34m   #     #     #   ######    #######   #   #    ####    #        #     ######      #      ####  ####')
    out('                                                                #      #                  ###    ###')
    out('                                                               #       #                  ##########\n')
    out("\033[36m[!] THANK YOU FOR USING THIS SOFTWARE! \033[;1m \033[94m")
    out('                                                        ------>')
    out('                                                        |')
    out('   #-------------------------------------------------------------->')
    out('                                                        |')
    out("                                                        ------>\n\033[92m")
    inf1 = 'This software is intended to be used with Debian and Ubuntu distros. To run the script, type "python3 start.py". Indicate whether you will be receiving or sending the encrypted messages. To change the destination IP or port or both, edit the "destip" and "destport" variables in the file "send.py". Messages take about 3 seconds to send and receive in this current version. \n\nThe connections are meant to be local and on the same network. This tool was designed to ease and secure communications with devices on local networks.\n\nIf you are facing errors, try running the following command to end any paused programs that might be interfering with TridEncrypt: "\033[91mkill -9 `jobs -ps`\033[92m". If that still doesn\'t work, make sure your system is up to date. Try deleting and reinstalling the software and make sure it has root privileges.\n'
    for x in inf1:
        time.sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()
    out('\n\033[94m       <------')
    out('             |')
    out('   <--------------------------------------------------------------#')
    out('             |')
    out('       <------')
except KeyboardInterrupt:
    print("[!] PROGRAM TERMINATED")
    exit()
