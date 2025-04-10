import socket


def send_file(filename, server_address=('192.168.11.129', 9000)): # Adresse IP de ma VM2 qui joue le role du serveur
    with open(filename, 'rb') as f, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        print(f"Envoi du fichier {filename}")
        while chunk := f.read(1024):
            sock.sendall(chunk)
        print("Fichier envoyé.")


if __name__ == "__main__":
    send_file("../Media/Projet L3.pdf")
