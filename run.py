#!/usr/bin/env python3

import locale
import os
import requests
import re
import json
import sys

url = 'http://34.121.234.105/fruits/'
os.chdir('supplier-data/descriptions/')

k_dicc = ['name', 'weight', 'description', 'image_name']

for doc in os.listdir():
    dicc = {}
    print(type(os.path.splitext(doc)[0]))
    nombre = os.path.splitext(doc)[0]+'.jpeg'
    with open(doc, encoding ='utf-8') as f:
        for i,line in enumerate(f):
            if k_dicc[i] == 'weight':
                dicc.setdefault(k_dicc[i], int(re.search(r'([0-9]+)', line.rstrip()).group()))
            elif i != 3:
                dicc.setdefault(k_dicc[i], line.rstrip())
        dicc.setdefault(k_dicc[3], nombre)
    print(dicc)
    r = requests.post(url, json=dicc)

