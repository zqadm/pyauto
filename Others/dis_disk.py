#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

data = {}
diskname_list = []
disk_list=[]


command = '''/usr/bin/awk '{print $3}' /proc/diskstats | /bin/egrep '^sd.*[a-z]$|^df.*[a-z]$|^nv.*[0-9]|^vd.*[a-z]$|^hd.*[a-z]$' | sort | uniq 2>/dev/null'''

lines = os.popen(command).readlines()

for line in lines:
        disk_name =  line.strip('\n')
        disk_list.append(disk_name)
for disk_name in list(set(disk_list)):
        disk_dict = {}
        disk_dict['{#DISK_NAME}'] = disk_name
        diskname_list.append(disk_dict)

data['data'] = diskname_list

jsonStr = json.dumps(data, sort_keys=True, indent=4)

print(jsonStr)

