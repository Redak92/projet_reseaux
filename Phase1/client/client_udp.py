import sys
import os
from protocols.UDP import UDPSocket
# Client UDP

SERVER_ADDR = ('192.168.10.2', 8081)
HOST_ADDR = ('192.168.10.1', 12345)

def main():
    server_address = SERVER_ADDR  # Adresse du serveur UDP (doit correspondre au serveur)

    sock = UDPSocket(*HOST_ADDR)
    while True:
        message = input("Entrez le message à envoyer (ou 'exit' pour quitter) : ")
        if message.lower() == 'exit':
            print("Fermeture du client.")
            break
        try:

            print(f"Envoi de {message} au serveur {server_address}")
            sock.sendto(message.encode(), server_address)  # Envoie le message au serveur

        except Exception as e:
            print(f"Erreur: {e}")


if __name__ == "__main__":
    main()
