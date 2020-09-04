#!/usr/bin/env python3

import requests
import os

url = 'http://localhost/upload/'
os.chdir('./supplier-data/images')

lista = [img for img in os.listdir() if os.path.splitext(img)[1] == '.jpeg']

for img in lista:
    with open(img, 'rb') as opened:
        r = requests.post(url, files={'file':opened})
