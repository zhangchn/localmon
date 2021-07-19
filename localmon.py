import socket
from psutil import cpu_percent
from datetime import datetime
from sys import exit

interval = 5.0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2003))
while True:
   percentage_for_cpus = cpu_percent(interval=interval, percpu=True) 
   print('%s' % percentage_for_cpus)
   ts = datetime.now().strftime('%s')
   for idx, p in enumerate(percentage_for_cpus):
       print('%d %f' % (idx, p))
       name = 'cpu_usage;cpu_num=%d' % idx
       sent = s.send(('%s %f %s\n' % (name, p, ts)).encode('ascii'))
       if sent == 0:
           exit(-1)
