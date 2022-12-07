#!/usr/bin/env python
#_*_ coding: utf8 _*_
 
from os import path
import dns.resolver

def subdomine():

	dominio = input("Please input a domine (format: domine.com): ")
	if path.exists('subdominios.txt'):
		words = open('subdominios.txt','r')
		words = words.read().split('\n')
		lista = []

		for i in words:
			try:
				dns.resolver.resolve('{}.'.format(i) + '.' + "dominio",'A')
				lista.append("{}.".format(i) + "." + dominio)
			except:
				pass

		if len(lista) > 0:
			print("Subdominios posibles: {}".format(len(lista)))
			for e in lista:
				print(e)
		else:
			print("No hay subdominios relacionados a este dominio")



if __name__ == '__main__':
	subdomine()