#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
import emails

def cpu_usage():
    if psutil.cpu_percent(10) > 1:
        return 'Error - CPU usage is over 80%'


def disk_usage():
    hdd = psutil.disk_usage('/')
    if 100/hdd.total*hdd.free < 20:
        return 'Error - Available disk space is less than 20%'


def available_memory():
    if psutil.virtual_memory().total/(10 ** 6) - psutil.virtual_memory().used/(10 ** 6) < 500:
        return 'Error - Available memory is less than 500MB'

def localhost_127():
    if socket.gethostbyname(socket.gethostname()) != '127.0.0.1':
        return 'Error - localhost cannot be resolved to 127.0.0.1'

while True:
    print('[ANALIZANDO]')
    msg = [cpu_usage(), disk_usage(), available_memory(), localhost_127()]
    for mensaje in msg:
        if mensaje != None:
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            subject = mensaje
            body = "Please check your system and resolve the issue as soon as possible."

            message = emails.generate_error_report(sender, receiver, subject, body)
            emails.send_email(message)



