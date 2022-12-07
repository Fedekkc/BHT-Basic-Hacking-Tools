#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse


def headers():
	target = input("Target: ")
	if target:
		try: 
			link = requests.get(url=target)
			headers = dict(link.headers)
			for i in headers:
				print(i + ": " + headers[i])
		except:
			print("Couldn`t connect with that url")

	else:
		print("There is no objective")
	


if __name__ == '__main__':
	headers()