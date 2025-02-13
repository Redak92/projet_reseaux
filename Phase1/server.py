import socket
import threading


def handle_tcp_client(client_socket, addr):
    with client_socket:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Send with TCP from IP : {addr[0]} with message {message}")

def tcp_server():
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.bind(('0.0.0.0', 8080))
    tcp_sock.listen(5)
    print("TCP server listening on port 8080")
    while True:
        client_socket, addr = tcp_sock.accept()
        client_handler = threading.Thread(target=handle_tcp_client, args=(client_socket, addr))
        client_handler.start()

def udp_server():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.bind(('0.0.0.0', 8081))
    print("UDP server listening on port 8081")
    while True:
        message, addr = udp_sock.recvfrom(1024)
        print(f"Send with UDP from IP : {addr[0]} with message {message.decode('utf-8')}")

tcp_thread = threading.Thread(target=tcp_server)
udp_thread = threading.Thread(target=udp_server)

tcp_thread.start()
udp_thread.start()

tcp_thread.join()
udp_thread.join()