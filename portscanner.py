#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear', shell=True)
server_name = raw_input("Enter a remote host to scan: ")
server_ip = socket.gethostbyname(server_name)
t1 = datetime.now()
try:
    for port in range(1,1025):
        network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = network_socket.connect_ex((server_ip, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        network_socket.close()
except KeyboardInterrupt:
    print "Process terminated"
    sys.exit()
except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
except socket.error:
    print "Couldn't connect to server"
    sys.exit()
# Checking the time again
t2 = datetime.now()
total = t2 - t1
print 'Port Scan Completed in: ', total
