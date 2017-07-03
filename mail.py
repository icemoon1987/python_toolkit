#!/usr/bin/env python
#coding: utf-8

import smtplib
import email
import mimetypes
import json
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText

mail_host = ""
mail_user = ""
mail_pwd = ""
mail_postfix = ""

def sendmail(to_list,subject,content):
  # translation
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEMultipart('related')
    msg['Subject'] = email.Header.Header(subject,'utf-8')
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    msg.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgText = MIMEText(content, 'plain', 'utf-8')
    msgAlternative.attach(msgText)
    msg.attach(msgAlternative)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pwd)
        s.sendmail(me, to_list, msg.as_string())
        s.quit() 
    except Exception,e:
        print e
        return False
    return True
    
def sendhtmlmail(to_list,subject,content):
  # translation
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEMultipart('related')
    msg['Subject'] = email.Header.Header(subject,'utf-8')
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    msg.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgText = MIMEText(content, 'html', 'utf-8')
    msgAlternative.attach(msgText)
    msg.attach(msgAlternative)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pwd)
        s.sendmail(me, to_list, msg.as_string())
        s.quit() 
    except Exception,e:
        print e
        return False
    return True

if __name__ == '__main__':

    detail = """
    """

    if sendhtmlmail(['panwenhai@100tal.com', 'lizhengtang@100tal.com'],"测试邮件", detail):
        print "Success!"
    else:
        print "Fail!"

    


