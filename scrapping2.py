

def scrapping2():
	web = open('web.html','r')

	start = input("Please input the start of the scrap: ")

	end = input("Please input the end of the scrap: ")

	for linea in web.readlines():
		if start in linea:
			print(linea)


if __name__ == '__main__':
	scrapping2()