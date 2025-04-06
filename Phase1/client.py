from IP.UDP import SocketUDP


class ClientUDP:
    def __init__(self, ip: str, port: int):
        self.socket = SocketUDP(ip)
        self.port = port

    def send_message(self, message: str):
        self.socket.send_udp((self.socket.ip, self.port), message.encode(), 54208)



if __name__ == "__main__":
    c = ClientUDP("127.0.0.1", 8081)
    c.send_message("Hello there")