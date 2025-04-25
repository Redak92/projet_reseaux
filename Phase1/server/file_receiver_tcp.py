import socket
import os

def receive_file(server_address=('0.0.0.0', 9000)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(server_address)
        sock.listen(5)
        print(f"Serveur en écoute sur {server_address[0]}:{server_address[1]}")

        os.makedirs("../received", exist_ok=True)

        while True:
            print("En attente d'une connexion entrante...")
            conn, addr = sock.accept()
            print(f"Connexion reçue de {addr}")
            with conn:
                file_path = f"../received/received_from_{addr[1]}.pdf"
                with open(file_path, 'wb') as f:
                    while data := conn.recv(1024):
                        f.write(data)
                print(f"Fichier reçu et enregistré dans {file_path}")

if __name__ == "__main__":
    receive_file()
