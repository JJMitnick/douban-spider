# -*-coding:utf-8-*-
# @time: 2020/5/2 13:21
# @author: Mitnick
# @description: 发邮件工具

import re
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import *


class Mail(object):
    def __init__(self):
        self.sender = SENDER
        self.password = PASSWORD
        self.smtp = None

    def __login(self):
        try:
            self.smtp = smtplib.SMTP(MAIL_HOST)
            self.smtp.login(self.sender, self.password)
        except Exception as err:
            raise err

    def send(self, receiver, subject, html):
        if not re.match(r'^.*?@.*?\.\w*(,)?$', receiver.strip()):
            raise ValueError('receiver %s is invalid' % str(receiver))

        if self.smtp is None or self.smtp.does_esmtp == 0:
            try:
                self.__login()
            except Exception as err:
                raise err

        if not html:
            return None
        if not receiver:
            return None

        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = Header('白夜监测', 'utf-8')
        msg['To'] = receiver

        try:
            msg.attach(
                MIMEText(html, 'html', _charset='utf8')
            )
            self.smtp.sendmail(self.sender, receiver, msg.as_string())
        except Exception as err:
            raise err

    def quit(self):
        try:
            if self.smtp:
                self.smtp.quit()
        except RuntimeError as err:
            print(str(err))
            pass
