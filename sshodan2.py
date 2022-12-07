


import sys
from shodan import Shodan


def sshodan2():
	api = Shodan(input("Please input your Sshodan apiKey"))
	
	host = api.host(input("Please input your host"))
	print('''
		IP: 	{}
		City: 	{}
		ISP: 	{}
		Org: 	{}
		Ports: 	{}


		'''.format(host['ip_str'],host['city'],host['isp'],host['org'],host['ports']))
	f = open('scan.txt','w+')

	for e in host['data']:
		lista = e.keys()
		for l in lista:
			f.write(str(e[l]))
	f.close()

if __name__ == '__main__':
	sshodan2()