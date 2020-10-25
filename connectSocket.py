import socket
import sys
#Here we made a socket instance and passed it two parameters.
#The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully.\n")
except socket.error as err:
    print("Socket creation failed. ERROR: %s" %str(err))
    sys.exit()

port = 80 #port number that http website generally listen on

#getting ip address of server to connect to it
try:
    host_ip = socket.gethostbyname('cheshire.cse.buffalo.edu')
except socket.gaierror:
    # this means could not resolve the host
    print("Error resolving host.\n")
    sys.exit()

# connecting to the server
try:
    s.connect((host_ip, port))
    print("Client has successfully connected to cheshire on port == %s" % (host_ip))
except socket.error as err:
    print("Client has failed to connected to cheshire. ERROR: %s" %str(err))
    sys.exit()
