from IP.UDP import SocketUDP


class ServerUDP:
    def __init__(self, ip: str, port: int):
        self.socket = SocketUDP(ip)
        self.port = port
    
    def receive_video(self):
        for packet in self.socket.receive_udp(self.port):
            data, addr = packet
            source_ip, source_port = addr

            
                



if __name__ == "__main__":
    s = ServerUDP("127.0.0.1", 8081)
    s.wait_for_client()