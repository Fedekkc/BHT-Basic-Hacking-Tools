#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver

def dns():


	target = input("Ingresa el target (formato URL www.xxxxxx.com): ")
	count = 0
	querys = ["A","NS","MD","MF","CNAME","SOA","MB","MG","MR","NULL","WKS","PTR","HINFO","MINFO","MX","TXT","AXFR","MAILB","MAILA","ANY"]
	meanings = [
	"Dirección de host: ","Servidor de nombres autorizado: ","Destino de correo: ","Reenviador de correo: ",
	"Nombre canónico para un alias: ", "Inicio de una zona de autorización: ", "Nombre de dominio de buzón: ",
	"Miembro de grupo de correo: ","Nombre de dominio de redenominación de correo: ", "RR nulo: ",
	"Descripción de servicio conocido: ", "Puntero de nombre de dominio: ", "Información de host: ",
	"Información de lista de buzón o correo: ", "Intercambio de correo: ", "Cadenas de texto: ",
	"Transferencia de una zona entera: ", "Registros relacionados con el buzón: ", "RR de agente de correo",
	"Todos los registros: "]

	for i in querys:
		count = count + 1
		try:
			b = dns.resolver.resolve(target,i)
			for q in b:
				print(meanings[count - 1],q)
		except:
			print("Ocurrio un error con la query de {}".format(meanings[count - 1]))
		
			
	#a = dns.resolver.resolve("animeflv.net","A")
	#for q in a:
	#	print("Direccion del servidor: {}".format(q))


if __name__ == '__main__':
	dns()