#!/usr/bin/python
# -*- coding: UTF-8 -*-

#参考文章 http://www.runoob.com/python/python-email.html


import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


sender = 'sunny0000008@ghbsunny.cn' #指定发送者,可以不是真实存在的邮箱，只是让用户看的
receivers = ['95140000@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱，真实存在的接收邮箱


msgRoot = MIMEMultipart('related')
#msgRoot['From'] = Header("ghbsunny", 'utf-8')  #相当于给发件人备注别名
#msgRoot['To'] =  Header("接收", 'utf-8')  #相当于给收件人备注别名
subject = 'ghbsunny Python SMTP 邮件测试 02'
msgRoot['Subject'] = Header(subject, 'utf-8')
 
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
 
 
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="https://blog.51cto.com/ghbsunny">ghbsunny 博客链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
# 指定图片为当前目录
fp = open('test.png', 'rb') # 执行脚本所在的目录下要有test.png图片
msgImage = MIMEImage(fp.read())
fp.close()
 
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test', 'rb').read(), 'base64', 'utf-8')  #执行脚本的路径下要有test文件
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
msgRoot.attach(att1)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

print("----------another methed,now send with someone e-mail-------------------")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

#参考文章 http://www.runoob.com/python/python-email.html

#如果本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。
#python需要支持ssl模块，否则邮件发送不成功,通过进入python命令行，然后执行import ssl 查看是否报错，报错就是ssl模块缺少，需要重新编译安装
#当你发现无法导入ssl的时候，首先检查一下，系统是否安装了openssl和openssl-devel，然后再进行编译安装

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='95140000@qq.com'    # 发件人邮箱账号，真实存在
my_pass = 'zcasunzusjisbdae'              # 发件人邮箱密码,注意这里不是qq登录密码，而是通过在邮箱的账号里设置生成的授权码为邮箱的密码
my_user='33300000@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText('填写邮件内容211','plain','utf-8')
        msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="菜鸟教程发送邮件测试"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")

print("--------------method 3 : it is same as method 2")

#!/usr/bin/python
import smtplib
import string

#python需要支持ssl模块，否则邮件发送不成功,通过进入python命令行，然后执行import ssl 查看是否报错，报错就是ssl模块缺少，需要重新编译安装
#当你发现无法导入ssl的时候，首先检查一下，系统是否安装了openssl和openssl-devel，然后再进行编译安装

HOST = "smtp.qq.com"
SUBJECT = "Test email from sunny python"
TO =  "33300000@qq.com"
FROM = "95140000@qq.com"
text = "it is good to sendmail by python"
BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
        ))
server =smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("951400020@qq.com","zcasunzusjisbdae") #这里的xxxxxx为发件邮箱的账号里生成的授权码
server.sendmail(FROM,[TO],BODY)
