#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re

m = requests.get('http://campus.meituan.com/#/main/intern/post')
m.encoding = 'utf-8'
a = m.text
print a
print re.search(unicode('"totalPages":1,"totalResults":0', 'utf-8'), a)
