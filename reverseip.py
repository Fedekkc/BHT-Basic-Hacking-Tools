#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

def reverseip():
	site = input("Please input a target to analyze: ")
	agent = {'UserAgent':'Firefox'}
	a = requests.get('https://viewdns.info/reverseip/?host={}&t=1'.format(site),headers = agent)
	b = BeautifulSoup(a.text,'html5lib')
	c = b.find(id="null")
	d = c.find(border="1")
	for l in d.find_all('tr'):
		print(l)



if __name__ == '__main__':
	reverseip()