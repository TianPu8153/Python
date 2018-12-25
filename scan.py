# -*- coding: utf-8 -*-
#!/usr/bin/python
'''　　多线程 Socket TCP 端口扫描器  by: EvilCLAY'''
import socket
import sys
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
remote_server = raw_input("Enter a remote host to scan:")
remote_server_ip = socket.gethostbyname(remote_server)
ports = []
ports_open=[]
# print '-' * 60
# print 'Please wait, scanning remote host ', remote_server_ip
# print '-' * 60
socket.setdefaulttimeout(0.5)
def scan_port(port):
    try:
        s = socket.socket(2,1)
        res = s.connect_ex((remote_server_ip,port))
        if res == 0: # 如果端口开启 发送 hello 获取banner
            ports_open.append(port)
            #print 'Port {}: OPEN'.format(port)
        #else:
            #print 'Port {}: CLOSE'.format(port)
        s.close()
    except Exception,e:
        print "Error:port-"+port
# for i in range(1,65535):
for i in (80,135,139,445,1433,2383,3306,3389,4899,5357,33606):
    ports.append(i)
# Check what time the scan started
t1 = datetime.now()
pool = ThreadPool(processes = 16)
results = pool.map(scan_port,ports)
pool.close()
pool.join()
time=datetime.now() - t1
print "Multiprocess Scanning Completed in"
print time
ports_open.sort()#排序
print ports_open