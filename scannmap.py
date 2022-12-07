
from nmap import PortScanner
import nmap


def scanmap():
	nm = nmap.PortScanner()
	ip = input("IP: ")
	escaneo = nm.scan(hosts=ip,arguments="--top-ports 1000 -sV --version-intensity 3")
	print("Resultados del escaneo: " + str(escaneo))
	print("Protocolos utilizados: {}".format(nm[ip].all_protocols()))
	print("Estado de la maquina: {}".format(nm[ip].state()))
	print(nm[ip]['tcp'])

	for e in nm[ip]['tcp'].keys():
		for d in nm[ip]['tcp'][e]:
			print(d + " : " + nm[ip]['tcp'][e][d])
			if(d == "cpe"):
				print("========================================")

	
	

 

if __name__ == '__main__':
	scanmap()