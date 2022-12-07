import hashlib


def passcrypt():
	password = str(input("Ingrese una contraseña a cifrar"))

	passwordcrypted = hashlib.md5(password.encode()).hexdigest()

	print(passwordcrypted)


if __name__ == '__main__':
	passcrypt()