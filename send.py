import socket

destip = "10.128.178.165" #CHANGE THIS TO THE DESTINATION IP
destport = 80  #CHANGE THIS TO THE DESTINATION PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recipient_addr = (destip, destport) # set the IP address and port number
securefile = open("Skeys.txt", "r")
mes = securefile.read()
bytes_sent = sock.sendto(mes.encode(), recipient_addr)
sock.close()
