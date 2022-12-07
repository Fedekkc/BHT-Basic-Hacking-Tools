#!/usr/bin/env python
#_*_ coding: utf8 _*_

from Wappalyzer import WebPage, Wappalyzer
import argparse



def wappalyzer():
	target = input("Please input the target to be analyzed: ")
	wap = Wappalyzer.latest()
	try:
		web = WebPage.new_from_url(target)
		tecnos = wap.analyze(web)
		for t in tecnos:
			print("Tecnologia detectada: {}".format(t))
	except e:
		print("ERROR: {}".format(e))



if __name__ == '__main__':
	try: 
		wappalyzer()
	except KeyboardInterrupt:
		exit()