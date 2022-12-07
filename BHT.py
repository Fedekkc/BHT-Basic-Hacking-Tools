#Código desarrollado por Federico Cacace. @Fedekkc en Github
#Code developed by Federico Cacace. @Fedekkc on github
#BHT = Basic Hacking Tools

from cloudflare import cloudflare
from dns1 import dns
import os
from forms1 import forms
from Headers import headers
from LFI import LFI
from passcrypt import passcrypt
from RCE import RCE
from reverseip import reverseip
from scannmap import scanmap
from scrapping import scrapping
from scrapping2 import scrapping2
from ssh import ssh
from sshodan import sshodan
from sshodan2 import sshodan2
from subdomines import subdomine
from wappalyzer import wappalyzer
from whois import whois
from worm import worm



def menu():
	print("--------------------------------------------")
	print("Bienvenido a BHT - Desarrollado por @Fedekkc")
	print("--------------------------------------------")
	print("\n\n\n")
	print("Herramientas disponibles: ")
	print("\
		1. Cloudflare detector\n\
		2. DNS Resolver\n\
		3. Forms Searcher\n\
		4. Headers Obtainer\n\
		5. Basic LFI\n\
		6. MAC changer\n\
		7. PassCrypter\n\
		8. RCE\n\
		9. Reverseip\n\
		10. Scanmap\n\
		11. Web scrapper\n\
		12. Web Scrapper 2\n\
		13. SSH Brute Force\n\
		14. Shodan\n\
		15. Shodan 2\n\
		16. Subdomine detector\n\
		17. Techno Detector\n\
		18. Whois\n\
		19. Worm")
	opcion = int(input("Opcion: "))
	if(opcion == 1):
		cloudflare()
	elif(opcion == 2):
		dns()
	elif(opcion == 3):
		forms()
	elif(opcion == 4):
		headers()
	elif(opcion == 5):
		LFI()
	elif(opcion == 6):
		os.system("python mac_changer.py")
	elif(opcion == 7):
		passcrypt()
	elif(opcion == 8):
		RCE()
	elif(opcion == 9):
			reverseip()
	elif(opcion == 10):
			scanmap()
	elif(opcion == 11):
		scrapping()
	elif(opcion == 12):
		scrapping2()
	elif(opcion == 13):
		ssh()
	elif(opcion == 14):
		sshodan()
	elif(opcion == 15):
		sshodan2()
	elif(opcion == 16):
		subdomine()
	elif(opcion == 17):
		wappalyzer()
	elif(opcion == 18):
		whois()
	elif(opcion == 19):
		worm()






def main():
	menu()



if __name__ == '__main__':
	main()
	



