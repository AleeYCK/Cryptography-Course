from cryptography.fernet import Fernet

mensaje = "Al infinito y más allá"
key = Fernet.generate_key()

f = Fernet(key)

enctex = f.encrypt(mensaje.encode())

dectex = f.decrypt(enctex).decode()

option = 0
def menu(option):
    menu = "¿Quieres leerlo?\n 1) Encriptar \n 2) Desencriptar \n 3) Salir"
 while option != 3:
        if option == 1:
            print(enctex)
        elif option == 2:
            print(dectex)

print(menu)
