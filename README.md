# python_hackathon

## Project
To create a script that will
1) Scan your OS and your device IP
2) Calculate how many hosts in your subnet are occupied/unoccupied
3) Check if your system is using any common ports (e.g. HTTP, HTTPS, NTP)
4) Locate the vendor for all of the occupied hosts in your subnet (e.g. Cisco, Apple)

## Getting Started

1) Run test.py to get started

'''

      dP                               dP
      88                               88
      88       .d8888b..d8888b..d8888b.88dP    dPd888888b.d8888b.88d888b.
      88       88'  `8888'  `""88'  `888888    88   .d8P'88ooood888'  `88
      88       88.  .8888.  ...88.  .888888.  .88 .Y8P   88.  ...88
      88888888P`88888P'`88888P'`88888P8dP`8888P88d888888P`88888P'dP
                                              .88
                                          d8888P


1. Scan your local network
2. Scan another network
Would you like to scan your local network or another network?
'''

Then based on your selection, a summarized report will be generated:

```
--------------------------------------------------
ABOUT YOUR SYSTEM:
==================================================
Host IP: <YOUR_HOST_UP>
Subnet-mask: <HOST_SUBNET>
Network IP: <NETWORK_IP>


NETWORK UTILIZATION:
....................
Occupied hosts: 	4
Unoccupied hosts: 	12
Total hosts on subnet: 	14


COMMON PORT AVAILABILITY:
....................
None of your common ports (from 1-1023) are open.


HARDWARE DISTRIBUTION:
....................

IP: 		<HOST_IP>
Company: 	Cisco Systems, Inc
MAC Prefix: 	4C:77:6D

IP: 		<HOST_IP>
Company: 	Cisco Systems, Inc
MAC Prefix: 	4C:77:6D

IP: 		<HOST_IP>
Company: 	Cisco Systems, Inc
MAC Prefix: 	68:2C:7B

IP: 		<HOST_IP>
Company: 	Apple, Inc.
MAC Prefix: 	8C:85:90
