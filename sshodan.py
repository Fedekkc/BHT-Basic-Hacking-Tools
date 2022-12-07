

import sys
from shodan import Shodan



def sshodan():
	
	apiKey = input("Please input your Sshodan apiKey")

	searcher = Shodan(apiKey)

	try:
		query = searcher.search("struts")
		print("Resultados: {}".format(query['total']))
		for host in query['matches']:
			print("===================================")
			print("ORG: {}".format(host['org']))
			print("IP: {}".format(host['ip_str']))
			print("Port: {}".format(host['port']))
			print("Location: {}".format(host['location']))
			print("Banner: {}".format(host['data']))
			try:
				print("ASN: {}".format(host['asn']))
			except:
				pass
			for l in host['location']:
				print(l+" : " + str(host['location'][l]))
			
	except:
		print("Hubo un error en la ejecución de la busqueda")

if __name__ == '__main__':
	sshodan()


