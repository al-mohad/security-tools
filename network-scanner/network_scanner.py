# Author: Muhammad Buhari
# GitHub: github.com/al-mohad
# Program: NETWORK SCANNER

import os
import scapy.all as scapy
import argparse


def get_arguements():
    parser =argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range. ")
    scoptions = parser.parse_args()
    return options


def scan_ip(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast =  scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]

    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n----------------------------------------------------------")
    for client in result_list:
        print(client["ip"] +"\t\t" + client["mac"])

options = get_arguements()
scan_result = scan_ip(options.target)
print(scan_result)