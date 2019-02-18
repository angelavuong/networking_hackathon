import socket
import os



local = '127.0.0.1'
mycomp = '10.150.55.26'


#function to find ports that are opened
#1st argument is the ip address of device to be checked
#2nd argument is a list of ports to be checked
def port_finder(ip_address, list_of_ports):
    list_of_open_ports = []
    for port in list_of_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip_address,port))
        # if port is open
        if result == 0:
            #if the port is open, append to list
            list_of_open_ports.append(port)


        s.close()
    #return a list of opened ports
    return list_of_open_ports



#dictionaries to hold mappings of most common well-known ports
def main(ip_add):
    well_known_ports = { 80 : 'HTTP',  443 : 'HTTPS',  53: 'DNS', 25 : 'SMTP',110: 'POP3',
     143: 'IMAP', 23: 'Telnet',  22: 'SSH',  119 : 'NNTP', 563: 'NNTPS', 194 : 'IRC', 123 : 'NTP',
     514: 'Syslog', 88: 'Kerberos', 137: 'NetBIOS'}

    #get a list of well_known_ports
    list_of_well_known_ports = list(well_known_ports.keys())

    #well known ports are in the range of 1 to 1023
    ports_open = port_finder(ip_add,list_of_well_known_ports)
    if ports_open == True:
        for port in ports_open:
            print "\n\nCOMMON PORT AVAILABILITY:"
            print "." * 20
            print('Port Open: ' + str(port) + '\tService: ' + well_known_ports[port])
    else:
        print "\n\nCOMMON PORT AVAILABILITY:"
        print "." * 20
        print 'None of your common ports (from 1-1023) are open.'
