"""

作业一：

背景： 网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，探测目标主机是否开放了指定端口（1-1024），用于改善目标主机的安全状况。

要求：编写一个基于多进程或多线程模型的主机扫描器。

使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
需考虑网络异常、超时等问题，增加必要的异常处理。
因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。
命令行参数举例如下：
pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100

pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json

说明：

因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
-n：指定并发数量。
-f ping：进行 ping 测试
-f tcp：进行 tcp 端口开放、关闭测试。
-ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
-w：扫描结果进行保存。

"""

import socket
from queue import Queue
import threading
import json


class GetIpThread(threading.Thread):
    def __init__(self, ip, queue, conn, file):
        super(GetIpThread, self).__init__()
        self.ip = ip
        self.queue = queue
        self.conn = conn
        self.file = file

    def run(self):
        while True:
            self.conn.acquire()
            if self.queue.empty():
                pass
            port = self.queue.get()
            ip_port = self.get_ip_status(self.ip, port)
            print('run:', ip_port)
            if not ip_port:
                pass

            json.dump(ip_port, fp=self.file, ensure_ascii=False)
            self.queue.task_done()
        self.conn.release()

    def get_ip_status(self, ip, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.settimeout(1)  # 设置超时时间
        isopen = False
        try:
            r = server.connect_ex((ip, port))
            isopen = r == 0
        finally:
            server.close()
            result = {
                'ip': ip,
                'port': port,
                'isopen': isopen
            }
            return result


if __name__ == '__main__':
    ip = '192.168.1.102'
    output = open('result.json', 'a', encoding='utf-8')

    portsQueue = Queue(2000)
    for pq in range(1, 1025):
        portsQueue.put(pq)

    conn = threading.Condition()

    for _ in range(10):
        thread = GetIpThread(ip, portsQueue, conn, output)
        thread.start()
