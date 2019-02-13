#!/usr/bin/env python
# coding: utf-8

import requests

r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
r.encoding = 'utf-8'
print(r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'])
