import socket


def main():
    server_address = ('localhost', 8080)  # Adresse du serveur TCP (doit correspondre au serveur)
    # Création du socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect(server_address)  # Établit une connexion avec le serveur
            print(f'Connecté au serveur {server_address}')

            while True:
                message = input("Entrez le message à envoyer (ou 'exit' pour quitter) : ")
                if message.lower() == 'exit':
                    print("Fermeture du client.")
                    break
                print(f"Envoi de {message} au serveur {server_address}")
                sock.sendall(message.encode())  # Envoie le message au serveur
                # Attendre une réponse du serveur
                data = sock.recv(1024).decode()
                print(f"Réponse du serveur : {data}")

        except Exception as e:
            print(f'Erreur: {e}')


if __name__ == "__main__":
    main()
