#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import smtplib
from email.mime.text import MIMEText

if __name__ == '__main__':
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    myaddr_ex = socket.gethostbyname_ex(myname)

    msg_str = str(myaddr) + '\n'+ str(myaddr_ex)
    msg = MIMEText(msg_str)
    msg['Subject'] = 'PC IP Address'
    msg['From'] = 'sender@xx.com'
    msg['To'] = 'receiver@xx.com'

    s = smtplib.SMTP('mail.xx.com')  # No SSL
    s.login('sender@xx.com', 'senderpassword')
    s.sendmail('sender@xx.com', ['receiver@xx.com'], msg.as_string())
    s.quit()
