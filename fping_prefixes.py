import sys, time, requests, json
from fping_api import *

time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")

#file for prefixes imported from NetBox
file = open('fping_prefixes', 'r+')

for prefixes in ip_prefix():
    file.write(str(prefixes) + '\n')
file.close