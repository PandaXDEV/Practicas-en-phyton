import hashlib

hash_file = "bc7a844476607e1a59d8eb1b1f311830"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

with open(dic_file, 'r') as file:

    diccionario = [line.strip() for line in file]

    for password in diccionario:

        hash_calculado = hashlib.md5(password.encode()).hexdigest()

        if hash_calculado == hash_file:

            print("La contraseña original es: " + password)
            break