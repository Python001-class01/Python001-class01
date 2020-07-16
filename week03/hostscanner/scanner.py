#! /usr/bin/python

import argparse
import re
import subprocess
import sys
import socket
import threading
import json
from concurrent.futures import ThreadPoolExecutor

PORT_RANGE = (0, 1024)

class HostScanner():
    def __init__(self, op, ip, save_file):
        self.op = op
        self.ip = ip
        self.file = save_file

    def start_ping(self, ip):
        cmd = "ping -c 3 {}".format(ip)
        pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        pipe.wait()

        if pipe.poll() == 0:
            return ip
        else:
            return None

    def start_tcp(self, host):
        try:
            s = socket.socket()
            s.settimeout(5)
            s.connect(host)
            # port_list.append(port)
        except Exception as e:
            print(f"connect {host} failed: {e}")
            s.close()
            return None
        print(f"connect success:{host}")
        s.close()
        return host

def parse_cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='the number of thread', required=True)
    parser.add_argument('-f', choices=['ping', 'tcp'], help='operation, ping or tcp', required=True)
    parser.add_argument('-ip', help='ip', required=True)
    parser.add_argument('-w', help='save result to file')

    args = parser.parse_args()

    ip = []
    if '-' in args.ip:
        ip = args.ip.split('-')
    else:
        ip.append(args.ip)
    
    for i in ip:
        if check_ip(i) == False:
            print("ip address format error")
            return (args.n, args.f, None, args.w)

    ip_list = []

    if len(ip) == 2:
            start = ip[0].split('.')
            end = ip[1].split('.')
            new_ip = ip[0].split('.')
            
            if start[:-1] != end[:-1]:
                print("ip range error")
                return (args.n, args.f, None, args.w)

            for i in range(int(start[-1]), int(end[-1]) + 1):
                new_ip[-1] = str(i)
                ip_list.append('.'.join(new_ip))
    else:
        ip_list = ip

    return (args.n, args.f, ip_list, args.w)

def check_ip(ipaddress):
    regex = r"^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$"

    compile_ip = re.compile(regex)
    if compile_ip.match(ipaddress):
        return True
    else:
        return False

def write_file(filename, content, mod):
    with open(filename, mod) as f:
        if isinstance(content,dict):
            json.dump(content, f)
        else:
            f.write(content)

def scanner_manager():
    number, operation, ip, is_write = parse_cmd()
    scanner = HostScanner(operation, ip, is_write)
    if scanner.ip == None:
        sys.exit(0)

    if scanner.op == "ping":
        with ThreadPoolExecutor(number) as executor:
            ping_result = executor.map(scanner.start_ping, scanner.ip)
    
        for r in ping_result:
            if r == None:
                continue
            elif scanner.file != None:
                write_file(scanner.file, r, 'a+')
            else:
                print(r)

    elif scanner.op == "tcp":
        host = []
        for ip in scanner.ip:
            for port in range(PORT_RANGE[0], PORT_RANGE[1]+1):
                host.append((ip, port))
        with ThreadPoolExecutor(number) as executor:
            tcp_result = executor.map(scanner.start_tcp, host)
        # tcp_result = scanner.start_tcp()
        host_json = {}
        port = []
        ip = ""
        
        if tcp_result == None:
            print("No port opened")
            sys.exit(1)
        for r in tcp_result:
            if r == None:
                continue
            old_ip = r[0]

            if ip != old_ip:
                port = []
                ip = old_ip
            port.append(r[1])
            host_json[r[0]] = port

        if scanner.file != None:
            write_file(scanner.file, host_json, 'w')
        else:
            print(host_json)

    else:
        print("-f operation error")
    


if __name__ == '__main__':
    scanner_manager()