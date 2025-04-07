import socket


def send_file(filename, server_address=('localhost', 9000)):
    with open(filename, 'rb') as f, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        print(f"Envoi du fichier {filename}")
        while chunk := f.read(1024):
            sock.sendall(chunk)
        print("Fichier envoyé.")


if __name__ == "__main__":
    send_file("../Media/Projet L3.pdf")
