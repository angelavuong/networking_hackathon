import os
import time
import subprocess
import ping, socket
import ipaddress
import sh
import nmap
from math import floor



def network_utilization(network_ip):
    num_subnet_hosts = 0
    list_host = []
    nm = nmap.PortScanner()

    nm.scan(hosts=str(network_ip), arguments='-n -sP')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    for addr in ipaddress.IPv4Network(network_ip):
        num_subnet_hosts += 1

    print "NETWORK UTILIZATION:"
    print "." * 20
    print "Occupied hosts: \t" + str(len(hosts_list))
    for host, status in hosts_list:
        # print('\t' + host + '\t' + status)
        list_host.append(host)
    print "Unoccupied hosts: \t" + str(num_subnet_hosts - len(hosts_list))
    print "Total hosts on subnet: \t" + str(num_subnet_hosts-2)
    percent_occupied = float(len(hosts_list)/num_subnet_hosts)
    percent_unoccupied = float(num_subnet_hosts - len(hosts_list) / num_subnet_hosts)

    return list_host
