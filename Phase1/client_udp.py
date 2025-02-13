import socket

def main():
    server_address = ('localhost', 8081)  

    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while True:
            message = input("Entrez le message à envoyer (ou 'exit' pour quitter) : ")
            if message.lower() == 'exit':
                print("Fermeture du client.")
                break
            try:
                
                print(f"Envoi de {message} au serveur {server_address}")
                sent = sock.sendto(message.encode(), server_address)

            except Exception as e:
                print(f"Erreur: {e}")

if __name__ == "__main__":
    main()