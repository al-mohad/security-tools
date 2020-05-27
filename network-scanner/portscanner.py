import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for inputs
remoteServer = input('Enter remote host to scan: ')
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information of which host we are about to scan
print('-' * 60)
print('Please wait, scanning remote host', remoteServerIP)
print('-' * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (scans all host between 1-1024)
# With some error handling for catching errors

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port {}: Open'.format(port))
        sock.close()
except KeyboardInterrupt:
    print('Program is interrupted by you!')
    sys.exit()
except socket.gaierror:
    print('Hostnamecould not found resolved. Exiting')
    sys.exit()
except socket.error:
    print('Could not connect to server')
    sys.exit()

# Checking the time again
t2 = datetime.now()
total = t2 - t1
print('\n')
print('-' * 60)
print('Scanning Completed in: ', total)
print('-' * 60)
