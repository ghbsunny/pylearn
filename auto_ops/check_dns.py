# encoding: utf-8
#! /usr/bin/python
'''
需要安装dns,pycurl 和httplib模块
wget http://www.dnspython.org/kits/1.9.4/dnspython-1.9.4.tar.gz
tar -zxvf dnspython-1.9.4.tar.gz
cd dnspython-1.9.4/
python setup.py install

yum install libcurl-devel -y
pip uninstall pycurl
export PYCURL_SSL_LIBRARY=openssl
pip install pycurl
httplib  is httplib upgrade
python httplib  pip install httplib
python 2 httplib
'''

import dns.resolver
import os
import httplib
iplist = []
domain = "www.hnsyun.com"
def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain,'A')
    except Exception, e:
        print('A error,now except')
        print("01 dns resolver error: " + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address)
    return True
def checkip(ip):
    checkurl = ip +":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET","/",headers={"Host":domain})
        r=conn.getresponse()
        getcontent = str(r.read(15))
    finally:
        if getcontent.find("DOCTYPE") != -1:
            print(ip + " [OK]")
        else:
            print(ip + " [ERROR]")
if __name__=="__main__":
 #   print(__name__)
    if get_iplist(domain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print("02 dns resolver error.")
