# Author: Muhammad Buhari
# GitHub: github.com/al-mohad
# Program: MAC CHANGER

import subprocess
import optparse
import re

print("[+] MAC Address Changer [+]")


def get_arguements():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change it's MAC Adress.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Adress.")
    parser.add_option("-e", "--example",
                      help="python3 mac_changer.py -i eth0 -m 00:33:er:66:22")
    (options, arguements) = parser.parse_args()
    if options.interface:
        parser.error(
            "[+] Please specify an Interface, use --help for more info [+]")
    elif not options.new_mac:
        parser.error(
            "[+] Please specify a new MAC, use --help for more info [+]")
    return options


def change_mac():
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguements()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_address_search_result = re.search(
    r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_address_search_result:
    print(mac_address_search_result.group(0))
else:
    print("[+] Could not read MAC address!!! [+]")

    # TODO:: Refactor code
