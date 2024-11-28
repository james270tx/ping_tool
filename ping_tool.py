# ping_tool.py by james270tx
# 
# Simple ping tool for locating devices on a /24 network
# Use the constants A, B, C, FIRST_HOST, and LAST_HOST to configure the range
#
# For future builds, to do lists includes support for multiple subnets and CIDR notation

import os

A = "192"
B = "168"
C = "0"
FIRST_HOST = 1
LAST_HOST = 254

def ping(address):
    return not os.system('ping %s -n 1' % (address,)) 

def pinger(subnet,first,last,active):
    for i in range(first, last+1):
        ip = subnet + str(i)
        if ping(ip):
            active.append(ip)

if __name__ == "__main__":
    print()
    print("Confirm you are running a Windows system. MacOS not supported")
    prompt = "Press 'y' to proceed: "
    confirm = input(prompt) 

    if confirm == 'y':
        total_hosts = LAST_HOST - FIRST_HOST + 1
        subnet = A + "." + B + "." + C +"."
        print("Confirm pinging", total_hosts, "hosts on", subnet+"0")
        confirm = input(prompt) 
        if confirm == 'y':
            active_hosts = []
            pinger(subnet,FIRST_HOST,LAST_HOST,active_hosts)    
        else:
            print("You pressed", confirm)
    else:
        print("You pressed", confirm)

    if len(active_hosts) > 0:
        print()
        print(len(active_hosts), "hosts found")
        for a in active_hosts:
            print(a)
    else:
        print("No hosts found")
    
    print("Exiting")
    print()