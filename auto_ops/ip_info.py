# encoding: utf-8
#! /usr/bin/env python
from IPy import IP
"""
安装IPy模块
wget https://pypi.python.org/packages/source/I/IPy/IPy-0.81.tar.gz --no-check-certificate
tar -zxvf IPy-0.81.tar.gz
cd IPy-0.81/
python setup.py install

根据输入的IP或子网返回网络、掩码、广播、反向解析、子网数、IP类型等信息"""

ip_s = raw_input('please input an IP or net-range: ')
ips=IP(ip_s)
if len(ips) > 1:
    print('net: %s' %ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse address: %s' %ips.reverseNames()[0])
print('hexadcimal: %s' % ips.strHex())
print('binary ip: %s' %ips.strBin())
print('iptype: %s' % ips.iptype())
