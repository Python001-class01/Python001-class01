import argparse
import re
import subprocess
import sys

class HostScanner():
    def __init__(self, threads, op, ip, save_file):
        self.threads = threads
        self.op = op
        self.ip = ip
        self.file = save_file

    def start_ping(self):
        ip_list = []
        if len(self.ip) == 2:
            start = self.ip[0].split('.')
            end = self.ip[1].split('.')
            new_ip = self.ip[0].split('.')
            for i in range(int(start[-1]), int(end[-1]) + 1):
                new_ip[-1] = str(i)
                ip_list.append('.'.join(new_ip))
        else:
            ip_list = self.ip

        for ip in ip_list:
            pipe = subprocess.Popen("ping -c 3 {}".format(ip), stdout=subprocess.PIPE, shell=True)
            pipe.wait()

            if pipe.poll() == 0:
                print("ping ip success: {}".format(ip))

    def start_tcp(self):
        pass
    
    def stop(self):
        pass

def parse_cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='the number of thread', required=True)
    parser.add_argument('-f', choices=['ping', 'tcp'], help='operation, ping or tcp', required=True)
    parser.add_argument('-ip', help='ip', required=True)
    parser.add_argument('-w', help='save result to file')

    args = parser.parse_args()

    # 正则检查ip
    ip = []
    regex = r"(2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2}(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}"
    matches = re.finditer(regex, args.ip, re.MULTILINE)
    
    for _, match in enumerate(matches, start=1):
        ip.append(match.group())
        if len(ip) > 2:
            print("ip address error")
            ip = None
            break
    return (args.n, args.f, ip, args.w)

if __name__ == '__main__':
    number, operation, ip, is_write = parse_cmd()
    scanner = HostScanner(number, operation, ip, is_write)
    if scanner.ip == None:
        sys.exit()
    if scanner.op == "ping":
        scanner.start_ping()
    elif scanner.op == "tcp":
        scanner.start_tcp()
    else:
        print("-f operation error")