#! /usr/bin/python3

from pymemcache.client.base import Client
from datetime import datetime
import time

mc_host = '192.168.56.103'
mc_port = 11211

mc = Client(f'{mc_host}:{mc_port}')

print(f'{datetime.now()}: Set key \'homework_num\' to memcached with expire = 5')
mc.set('homework_num', 'homework_11.2', expire=5)
time.sleep(1)
print(f'{datetime.now()}: Try to get key \'homework_num\' from memcached (1 sec)')
print(f"\'homework_num\' = {mc.get('homework_num')}")

time.sleep(5)
print(f'{datetime.now()}: Try to get key \'homework_num\' from memcached (6 sec)')
print(f"\'homework_num\' = {mc.get('homework_num')}")
