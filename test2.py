#!/usr/bin/env python3 

import textfsm

traceroute = '''
JKT-GANDUL-ME3600-UPE-01#traceroute mpls ipv4 192.168.82.64/32
Type escape sequence to abort.
  0 172.16.100.130 MRU 9000 [Labels: 287635 Exp: 0]
L 1 172.16.100.129 MRU 9000 [Labels: 16082 Exp: 0] 4 ms
L 2 172.16.100.125 MRU 9100 [Labels: 25399 Exp: 0] 0 ms
L 3 172.23.52.165 MRU 9186 [Labels: 25911 Exp: 0] 16 ms
L 4 172.23.11.242 MRU 9100 [Labels: 650344 Exp: 0] 16 ms
L 5 192.168.82.14 MRU 9192 [Labels: 662387 Exp: 7] 48 ms
L 6 192.168.82.48 MRU 9192 [Labels: 433680 Exp: 7] 56 ms
L 7 192.168.82.50 MRU 9014 [Labels: implicit-null Exp: 0] 64 ms
! 8 192.168.82.64 48 ms
'''

with open('trace.template') as template:
    fsm = textfsm.TextFSM(template)
    results = fsm.ParseText(traceroute)


for result in results:
    if(not result[2]):
        MTU = 0
    else:
        MTU = result[2]
    print(f'Hop #{result[0]} IP P2P {result[1]} MTU {MTU}')