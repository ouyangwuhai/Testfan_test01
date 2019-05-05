#!/usr/bin/env python

import unittest
import HTMLTestRunner
import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.application import MIMEApplication

#导入案例文件时，如果提示红线，则设置存放案例文件的文件夹mytestcase文件夹上一层目录pyunittest
#右击Mark Directory as ...  -> Source root则会
from mytestcase import TryBaidu
from mytestcase import TryTestfan
import os

mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(TryBaidu.BaiduTest))
mysuite.addTest(unittest.makeSuite(TryTestfan.Testfan))
reportname = "C:\\Users\\Administrator\\.jenkins\workspace\\Testfan_demo01\\Report\\runcases_result.html"
fp = open(reportname,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="综合测试结果",description="测试结果")
runner.run(mysuite)
fp.close()
