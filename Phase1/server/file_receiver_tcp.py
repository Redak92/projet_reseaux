import socket

def receive_file(server_address=('0.0.0.0', 9000)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(server_address)
        sock.listen(5)
        print(f"Serveur en écoute sur {server_address[0]}:{server_address[1]}")

        while True:
            print("En attente d'une connexion entrante...")
            conn, addr = sock.accept()
            print(f"Connexion reçue de {addr}")
            with conn:
                with open(f"received_from_{addr[1]}.pdf", 'wb') as f:
                    while data := conn.recv(1024):
                        f.write(data)
                print("Fichier reçu.")

if __name__ == "__main__":
    receive_file()
