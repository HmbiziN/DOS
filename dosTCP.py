import socket
import os

bytes = os.urandom(50000)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
uri="00.000.00.00"
port = 00
destination = (uri, port)

print("Tentative de connexion à {}:{}".format(uri, port))
my_socket.connect(destination)
print("Connexion réussie.")

while True:
    try:
        print("Envoi de données à {}:{}".format(uri, port))
        my_socket.send(bytes)
        print("Données envoyées avec succès.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'envoi des données:", e)
