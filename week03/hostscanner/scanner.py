import argparse

class HostScanner():
    def __init__(self, threads, op, ip, save_file):
        self.threads = threads
        self.op = op
        self.ip = ip
        self.file = save_file

    def start(self):
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
    # 提取ip为列表

    return (args.n, args.f, args.ip, args.w)

if __name__ == '__main__':
    number, operation, ip, is_write = parse_cmd()
    scanner = HostScanner(number, operation, ip, is_write)