#!/usr/bin/env python3
from configparser import ConfigParser
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

def TacacsTelnetTo(NodeID, commands):
    section = 'tacacs-aji'
    filename = '.conf/tacacs.ini'
    parser = ConfigParser()
    parser.read(filename)
    device = {}
    device['host'] = NodeID
    device['device_type'] = 'cisco_ios_telnet'
    params = parser.items(section)
    for param in params:
        device[param[0]] = param[1]
    result = {}
    try:
        with ConnectHandler(**device) as telnet:
            telnet.enable()
            for command in commands:
                output = telnet.send_command(command)
                result[command] = output
        return result
    except(NetmikoTimeoutException, NetmikoAuthenticationException) as Err:
        print(Err)
        return False
    
def j2mTelnetTo(NodeID, commands):
    section =  'j2m'
    filename = '.conf/tacacs.ini'
    parser = ConfigParser()
    parser.read(filename)
    device = {}
    device['host'] = NodeID
    device['device_type'] = 'cisco_ios_telnet'
    params = parser.items(section)
    for param in params:
        device[param[0]] = param[1]
    result = {}
    try:
        with ConnectHandler(**device) as telnet:
            telnet.enable()
            for command in commands:
                output = telnet.send_command(command)
                result[command] = output
        return result
    except(NetMikoTimeoutException, NetmikoAuthenticationException) as Err:
        print(Err)
        return False