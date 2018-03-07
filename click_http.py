#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen

url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/'
resp = urlopen(url)
code = resp.getcode()
if code==200:
    print('the page can be opened : code=',code)
else:
    print("Failed open...")
