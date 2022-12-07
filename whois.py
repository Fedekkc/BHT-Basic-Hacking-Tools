#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

def whois():
	target = inpput("Please input a target to be analyzed: ")
	a = requests.get("https://who.is/whois/{}".format(target))
	sopa = BeautifulSoup(a.text,'html5lib')
	for i in sopa.find_all("pre"):
		print (i.get_text())


if __name__ == '__main__':
	whois()