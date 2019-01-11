#!/usr/bin/env python

import unittest
import HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

#导入案例文件时，如果提示红线，则设置存放案例文件的文件夹mytestcase文件夹上一层目录pyunittest
#右击Mark Directory as ...  -> Source root则会
from mytestcase import TryBaidu
from mytestcase import TryTestfan

mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(TryBaidu.BaiduTest))
mysuite.addTest(unittest.makeSuite(TryTestfan.Testfan))
reportname = "result.html"
fp = open(reportname,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="综合测试结果",description="测试结果")
runner.run(mysuite)

#发送邮件
#基本信息配置
smtpserver = 'smtp.qq.com'        #发件人邮箱服务器
username = '303423249@qq.com'     #发件人邮箱地址
password = 'qthyfnszdkesbgfb'     #密码是邮箱使用客户端的授权码
sender = '303423249@qq.com'       #发件人邮箱地址
receiver = ['303423249@qq.com']   #收件人邮箱地址
subject = 'Python email test'     #邮件主题
mailbody = "Hi!\nHow are you?\nHere is your report" #邮件正文
attachfile = reportname             #邮件附件

#构造邮件内容
msg = MIMEMultipart('mixed')     #创建MIMEMultipart邮件对象，类型为mixed
msg['Subject'] = subject         #主题赋值
msg['From'] = '303423249@qq.com <303423249@qq.com>' #发件人赋值
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)   #收件人赋值

# 构造文字内容
text_plain = MIMEText(mailbody, 'plain', 'utf-8')
msg.attach(text_plain)

# 构造附件
sendfile = open(attachfile, 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# text_att["Content-Disposition"] = 'attachment; filename="smail.py"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename=attachfile)
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
