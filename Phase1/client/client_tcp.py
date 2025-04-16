from protocols.TCP import TCPSocket

HOST_ADDR = "192.168.10.1"
HOST_PORT = 12345
SERV_ADDR = '192.168.10.2'
SERV_PORT = 8080  # Adresse du serveur TCP (doit correspondre au serveur)

print("Heyy")
# Client TCP
def main():
    sock = TCPSocket(src_ip=HOST_ADDR, src_port=HOST_PORT)

    settings = sock.handshake(SERV_ADDR, SERV_PORT)
    settings = sock.send_data_terminal(SERV_ADDR, SERV_PORT, settings[0], settings[1], settings[2])
    sock.end_tcp(SERV_ADDR, SERV_PORT, settings[0] + 1, settings[1], settings[2])

if __name__ == "__main__":
    main()
