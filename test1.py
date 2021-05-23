#!/usr/bin/env python3
from connect import (
    TacacsTelnetTo,
    j2mTelnetTo
)

from sys import argv

import time
import textfsm

start_time = time.time()
src = argv[1]
dst = argv[2]
auth = argv[3]
#commands = ['show ip int brief',
#            'show int description',
#            'show ip ospf neighbor'
#           ]
commands = [f'traceroute mpls ipv4 {dst}/32 sou {src}']
if auth == 'tacacs':
    result = TacacsTelnetTo(src, commands)
elif auth == 'j2m':
    result = j2mTelnetTo(src, commands)

output = result[commands[0]].rstrip()

with open('trace.template') as template:
    fsm = textfsm.TextFSM(template)
    results = fsm.ParseText(output)

for result in results:
    if(not result[2]):
        MTU = 0
    else:
        MTU = result[2]
    print(f'Hop #{result[0]} IP P2P {result[1]} MTU {MTU}')

duration = time.time() - start_time
print('it takes about {:.2f} sec'.format(duration))
