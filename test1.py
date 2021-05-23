#!/usr/bin/env python3
from connect import (
    TacacsTelnetTo,
    j2mTelnetTo
)

from sys import argv

import time

start_time = time.time()
host = argv[1]
auth = argv[2]
commands = ['show ip int brief',
            'show int description',
            'show ip ospf neighbor'
           ]
if auth == 'tacacs':
    result = TacacsTelnetTo(host, commands)
elif auth == 'j2m':
    result = j2mTelnetTo(host, commands)

print(result)
duration = time.time() - start_time
print('it takes about {:.2f} sec'.format(duration))
