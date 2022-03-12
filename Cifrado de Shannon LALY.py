mensaje = "Adiós mundo cruel"

llave = "rjcsaohehcjnaeuja"


def c(llave, mensaje):
    return [chr(ord(a) ^ ord(b)) for (a, b) in zip(mensaje, llave)]


mensaje_encriptado = "". join(c(llave, mensaje))

decrypted = [chr(ord(a) ^ ord(b)) for (a, b) in zip(mensaje_encriptado, llave)]
"". join(decrypted)

option = 0
while(option!=3):
    if option == 1:
        print(c)
    elif option == 2:
        print(decrypted)
    print(" 1) Encriptar \n 2) Desencriptar \n 3) Salir")
    option = int(input("Pon un número"))

menu = "Leer mensaje"

print(menu)
