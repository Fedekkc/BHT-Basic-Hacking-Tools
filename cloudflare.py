#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests

def cloudflare():
	word = "cloudflare"
	url = requests.get(input("Introduzca la url del sitio: "))
	headers= dict(url.headers)
	print(headers)
	verif = False
	for h in headers:
		if headers[h].lower():
			verif = True
			break
	if verif == True:
		print("[-] El sitio está protegido por cloudflare")
	else:
		print("[+] El sitio no tiene cloudflare")






if __name__ == '__main__':
	cloudflare()