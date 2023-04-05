Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@HamptonJake 
UTEP-jescamilla2-CS4375
/
nets-tcp-framing
Public
Fork your own copy of UTEP-jescamilla2-CS4375/nets-tcp-framing
Code
Issues
Pull requests
Projects
Security
Insights
nets-tcp-framing/src/server.py /
@jescamilla2
jescamilla2 complete
Latest commit 718cf0c last week
 History
 1 contributor
Executable File  61 lines (45 sloc)  1.6 KB
 

#! /usr/bin/env python3

# server program

import socket, sys, re
sys.path.append("../lib")       # for params
import params
import mytar

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "server"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

conn, addr = s.accept() # wait until incoming connection request (and accept it)
print('Connected by', addr)

data = bytearray()
while 1:

    buf = conn.recv(1024)
    data += buf
    if len(buf) == 0:
        print("Zero length read, nothing to send, terminating")
        break
    sendMsg = ("Echoing %s" % data).encode()
    print("Received '%s', sending '%s'" % (data, sendMsg.decode()))
    while len(sendMsg):
        bytesSent = conn.send(sendMsg)
        sendMsg = sendMsg[bytesSent:0]

    '''
    if os.fork() == 0:      # child becomes server
        print('Connected by', addr)
        os.write(1, 'Message to send: '.encode())  # user enters message
        message = os.read(1, 1000)                 # read the message
        framer.send_msg(conn, message)
    '''

# data has been successfully received at this point. extract the data.
mytar.x(data)
    
conn.shutdown(socket.SHUT_WR)
conn.close()
        

        
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
nets-tcp-framing/server.py at master · UTEP-jescamilla2-CS4375/nets-tcp-framing