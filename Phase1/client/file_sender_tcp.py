from protocols.TCP import TCPSocket

HOST_ADDR = "192.168.10.1"
HOST_PORT = 12345

def send_file(filename, server_address=('192.168.10.2', 9000)):  # Adresse IP de ma VM2 qui joue le role du serveur
    sock = TCPSocket(HOST_ADDR, HOST_PORT)
    with open(filename, 'rb') as f:
        settings = sock.handshake(server_address[0], server_address[1])
        print(f"Envoi du fichier {filename}")
        while chunk := f.read(1024):
            settings = sock.send_data(server_address[0], server_address[1], settings[0], settings[1], settings[2], chunk)
        print("Fichier envoyé.")

    sock.end_tcp(server_address[0], server_address[1], settings[0] + 1, settings[1], settings[2])


if __name__ == "__main__":
    send_file("Media/Projet L3.pdf")
