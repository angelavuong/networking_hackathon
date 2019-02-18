import pprint
import requests
from subprocess import Popen, PIPE
import re
import json

def ip_to_mac(hosts_list):
    mac_list = []
    for host in hosts_list:
        pid = Popen(["arp", "-n", host], stdout=PIPE)
        s = pid.communicate()[0]
        mac = re.search(r"(([a-f\d]{1,3}\:){5}[a-f\d]{1,3})", s).groups()[0]
        mac_list.append(mac)
    return mac_list

def mac2oui_api(mac_list, host_list):
    i = 0
    apple_counter = 0
    intel_counter = 0
    cisco_counter = 0
    murata_counter = 0

    print '\n\nHARDWARE DISTRIBUTION:'
    print "." * 20
    for mac in mac_list:
        MAC_URL = 'http://macvendors.co/api/%s'
        r = requests.get(MAC_URL % mac).text
        ## REQUESTS.GET(MAC_URL % MAC).JSON
        print "\nIP: \t\t" + str(host_list[i])
        # pprint.pprint(r.json())
        r = json.loads(r)
        result =  r[u'result']
        for i_result in result:
            if (i_result == 'company'): # Key
                print "Company: \t" + str(result[i_result])
            elif (i_result == 'mac_prefix'):
                print ("MAC Prefix: \t" + str(result[i_result]))
            if('company' not in result):
                print "Company: \tN/A"
                print "MAC Prefix: \tN/A"

        ## DO API CALL > RAISE_FOR_STATUS

        # for i_result in result:
        #     print i_result

        i += 1
