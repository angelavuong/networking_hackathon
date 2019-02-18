import os
import re
import sys
from itertools import chain
import ipaddress
from ipaddress import (ip_network, IPv4Address, IPv4Network)
from netaddr import IPAddress

import network_utilization as a
import ports_utilization as b
import convertHex2Dec as c
import mac_oui as d

os_type = ''

def check_operating_system(): # Checks the running systems OS
    global os_type
    from sys import platform
    if platform == 'darwin':
        os_type = 'MAC'
    elif platform == 'win32':
        os_type = 'PC'
    return os_type

    ### NEED TO IMPLEMENT LINUX

def pull_host_log(): # Runs ipconfig/ifconfig for local machine
    os_type = check_operating_system()

    if(os_type == 'MAC'):
        hostfile = os.popen('ifconfig en0').read()
    elif(os_type == 'PC'):
        hostfile = os.popen('ipconfig').read()
    return hostfile

    ### GIVE USER OPTIONS TO PICK YOUR ADAPTER

def regex_host_ip_mask(): # Pulls host IP, subnet, and broadcast IP
    global os_type

    hostfile = pull_host_log()

    if(os_type == 'MAC'): # Pulls IPv4 Address, Subnet Mask
        ip_regex = re.compile(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) netmask (.*) broadcast')
        host_log_mac = ip_regex.findall(hostfile)
        host_log = list(chain.from_iterable(host_log_mac))

    elif(os_type == 'PC'): # Pulls IPv4 Address, Subnet Mask, Default Gateway
        ip_regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        host_log = ip_regex.findall(hostfile)
    return host_log

def locate_host_ip(host_log): # Find the host IP
    for i in range(len(host_log)):
        if ('.' in host_log[i]):
            return host_log[i]

def locate_host_subnet(host_log): # Find subnet mask
    for i in range(len(host_log)):
        if (host_log[i]).startswith('0xf'):
            subnet_mask = c.convert_hex_to_binary(host_log[i])
            return subnet_mask

def check_block_size(subnet_mask):
    if('128' in subnet_mask):
        return 128
    elif('192' in subnet_mask):
        return 64
    elif('224' in subnet_mask):
        return 32
    elif('240' in subnet_mask):
        return 16
    elif('248' in subnet_mask):
        return 8
    elif('252' in subnet_mask):
        return 4
    elif('254' in subnet_mask):
        return 2
    else:
        return 1


if __name__ == '__main__':
    list_host = []
    user_input = 0

    print '''
      dP                               dP
      88                               88
      88       .d8888b..d8888b..d8888b.88dP    dPd888888b.d8888b.88d888b.
      88       88'  `8888'  `""88'  `888888    88   .d8P'88ooood888'  `88
      88       88.  .8888.  ...88.  .888888.  .88 .Y8P   88.  ...88
      88888888P`88888P'`88888P'`88888P8dP`8888P88d888888P`88888P'dP
                                              .88
                                          d8888P

    '''



    print "1. Scan your local network"
    print "2. Scan another network"

    ## WHILE LOOP START
    user_input = raw_input("Would you like to scan your local network or another network? ")
    print ""
    ## WHILE LOOP END

    if(user_input == 1):
        host_log = regex_host_ip_mask()
        ip_addr = locate_host_ip(host_log)
        subnet_mask = locate_host_subnet(host_log)
        cidr = IPAddress(subnet_mask).netmask_bits()
        network_ip = ipaddress.ip_network(unicode(ip_addr + '/' + str(cidr)), strict=False)

    elif(user_input == 2):
        ip_addr = raw_input("Please enter the IP you want to analyze: ")
        subnet_mask = raw_input("Please enter the subnet mask (e.g. 255.255.255.0): ")
        cidr = IPAddress(subnet_mask).netmask_bits()
        print cidr
        network_ip = ipaddress.ip_network(unicode(ip_addr + '/' + str(cidr)), strict=False)

    print '-' * 50
    print "ABOUT YOUR SYSTEM:"
    print '=' * 50
    print "Host IP: " + str(ip_addr)
    print "Subnet-mask: " + str(subnet_mask)
    print "Network IP: " + str(network_ip)
    print '\n'

    ## DOT FORMAT

    # Prints number of occupied/unoccupied IPs in subnet
    list_host = a.network_utilization(network_ip)

    # Prints open common ports
    b.main(ip_addr)

    # Returns occupied MAC addresses
    list_mac = d.ip_to_mac(list_host)

    # Print hardware distribution
    d.mac2oui_api(list_mac, list_host)
