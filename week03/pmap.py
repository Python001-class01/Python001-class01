# 作业一：
# 背景： 网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，探测目标主机是否开放了指定端口，用于改善目标主机的安全状况。
# 要求：编写一个基于多进程或多线程模型的主机扫描器。
# 使用扫描器可以基于 ping 命令快速检测一个 ip 段是否可以 ping 通，如果可以 ping 通返回主机 ip，如果无法 ping 通忽略连接。
# 使用扫描器可以快速检测一个指定 ip 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
# ip 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
# 需考虑网络异常、超时等问题，增加必要的异常处理。
# 因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。
# 命令行参数举例如下：
# pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
# pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json

# 说明：
# 因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 python 自带的 socket 套接字。
# -n 参数 并发数量。
# -f ping 进行 ping 测试， -f tcp 进行 tcp 端口开放、关闭测试。
# ip 连续 ip 地址支持 192.168.0.1-192.168.0.100 写法。
# -w 扫描结果进行保存。
# 选做：
# 通过参数 [-m proc|thread] 指定扫描器使用多进程或多线程模型。
# 增加 -v 参数打印扫描器运行耗时 (用于优化代码)。
# 扫描结果显示在终端，并使用 json 格式保存至文件。
# 参考：https://docs.python.org/zh-cn/3/library/subprocess.html
# 
# 测试命令1：python pmap.py -n 2 -f ping -ip 192.168.0.1-192.168.0.33
# 测试命令2：python pmap.py -n 2 -f tcp -ip 192.168.0.33

import subprocess,os
import fire
import socket
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from ipaddress import ip_address

success_ports = []
ip_used=[]
lock = threading.Lock()

def ping_one(oneip):

    """
    ping单个ip地址，打印出有效的ip地址
    """
    try:
        res = subprocess.call('ping -n 2 -w 5 %s' % oneip, stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
        # 打印运行结果
        #print(oneip, True if res == 0 else False)
        if lock.acquire():
            if res == 0:
                ip_used.append(oneip)
            #else:
                #ip_not_used.append(ip)
            lock.release()
        #print(ip_address)
        
        #t=f"ping  {ip_address}"
        #if os.system(t) == 0:


        #res = subprocess.run(["ping", ip_address, "-t", "2"] , capture_output=True)
        #if res.returncode == 0:
           # print(ip_address)
           # ping_ok.append(ip_address)
            
    except Exception as e:
       # print("Something is wrong when you run the command 'ping'" , "0000000000",e)
       print(e)

def tcp_one(ip_port_tuple):

    """
    用socket连接ip地址及端口，参数 ip_port_tuple 为一个元祖
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    # connect to remote host
    try:
        
        s.connect(ip_port_tuple)
        return_code=0
        #result = '{0} port {1} is open'.format(ip, port)
        #return_code = s.connect_ex(ip_port_tuple)
    except Exception as e:
        print('Error:', e)
    if lock.acquire():  
        if return_code == 0:
            port_ok=ip_port_tuple[1]
            success_ports.append(port_ok)
        lock.release()

    

def ping_func(n, f, ip):

    """
    把ip地址格式标准化，用map方式加入线程池
    """
    if f == 'ping':

        #two parts
        if "-" in ip:
            seed=[]
            ip_start, ip_end = ip.split('-')
            ip_start = ip_address(ip_start)
            ip_end = ip_address(ip_end)
            while ip_start <= ip_end:
                #IP_QUEUE.put(str(ip_start))
                seed.append(str(ip_start))
                ip_start += 1
            '''
            k=start_ip.split(".")
            start_last_num = k[-1]
           
            print(start_last_num)

            h=stop_ip.split('.')
            stop_last_num = h[-1]
            before = ".".join(k[:3])
            print(stop_last_num,before)

            seed = [before + '.' + str(num) for num in range(int(start_last_num), int(stop_last_num)+1)]
            #print(seed)
        '''
        else:
            seed=[ip]
            #print(seed)

        with ThreadPoolExecutor(n) as executor:
            executor.map(ping_one, seed)
        

    elif f == 'tcp':
        seed = [(ip, port) for port in range(0, 14)]
        with ThreadPoolExecutor(n) as executor:
            executor.map(tcp_one, seed)
        print(f'IP地址{ip}的所有开放端口是：{success_ports}\n')
    else:
        print("You can only call 'ping' or 'tcp' function!")

fire.Fire(ping_func)
print(ip_used)



'''
import time
import threading
import subprocess
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from ipaddress import ip_address
 
 
def get_ip_list(ip_start, ip_end):
    # 创建一个队列
    IP_QUEUE = Queue()
    ip_used = []
    ip_not_used = []
    ip_start = ip_address(ip_start)
    ip_end = ip_address(ip_end)
    while ip_start <= ip_end:
        IP_QUEUE.put(str(ip_start))
        ip_start += 1
 
    # 定义一个执行 ping 的函数
    def ping_ip(ip):
        res = subprocess.call('ping -n 2 -w 5 %s' % ip, stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
        # 打印运行结果
        print(ip, True if res == 0 else False)
        if lock.acquire():
            if res == 0:
                ip_used.append(ip)
            else:
                ip_not_used.append(ip)
            lock.release()
 
    # 创建一个最大任务为100的线程池
    pool = ThreadPoolExecutor(max_workers=120)
    lock = threading.Lock()
    start_time = time.time()
    all_task = []
    while not IP_QUEUE.empty():
        all_task.append(pool.submit(ping_ip, IP_QUEUE.get()))
    # 等待所有任务结束
    wait(all_task, return_when=ALL_COMPLETED)
    print('ping耗时：%s' % (time.time() - start_time))
    return ip_used, ip_not_used
 
 
if __name__ == '__main__':
    ip_used, ip_not_used = get_ip_list("202.169.50.1", "202.169.51.255")
    print(str(len(ip_used))+"已用", "\n", ip_used)
    print(str(len(ip_not_used))+"未用", "\n", ip_not_used
————————————————
版权声明：本文为CSDN博主「杰克小麻雀」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/yushuaigee/java/article/details/85244394

'''