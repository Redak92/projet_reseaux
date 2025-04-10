import socket


def receive_file(save_path='../received/received_file.pdf', server_address=('0.0.0.0', 9000)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(server_address)
        sock.listen(1)
        print('Waiting for connexion')
        conn, addr = sock.accept()
        print(f"Connexion de {addr}")
        with open(save_path, 'wb') as f:
            while data := conn.recv(1024):
                f.write(data)
        print("Fichier reçu.")


if __name__ == "__main__":
    receive_file()
