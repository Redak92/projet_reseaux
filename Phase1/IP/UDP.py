from .socket_IP import SocketIP
from .socket_IP import BASE_IP
import socket
class SocketUDP(SocketIP):
    def __init__(self, ip: str = BASE_IP):
        print(f" [UDP] Binded on {ip} ")
        super().__init__(ip)
        self.protocol = 0x11
    def build_udp_header(self, source_port: int, destination_port: int, data: bytes):
        source_port_bytes = source_port.to_bytes(2, byteorder='big')
        destination_port_bytes = destination_port.to_bytes(2, byteorder='big')
        length = 8 + len(data)
        length_bytes = length.to_bytes(2, byteorder='big')
        checksum = 0
        checksum_bytes = checksum.to_bytes(2, byteorder='big')
        packet = source_port_bytes + destination_port_bytes + length_bytes + checksum_bytes + data
        packet = self.put_checksum(packet, 6, 2)
        return packet
    def send_udp(self, target_address: tuple[str,int], data: bytes, source_port: int = 12345):
        destination_port = target_address[1]
        udp_header = self.build_udp_header(source_port, destination_port, data)
        self.sendall(target_address, udp_header, self.protocol)
    def receive_udp(self, max=65535):
        while True:
            print("Listening for incoming packets...")
            packet, _ = self.reicv_socket.recvfrom(max)
            source_ip, _, data = self.decapsulate_ip(packet)
            source_port = int.from_bytes(packet[20:22], byteorder='big')
            destination_port = int.from_bytes(packet[22:24], byteorder='big')
            print(f"Packet received from {source_ip} on port {source_port} : {data.decode()}")
            print(f"Destination port : {destination_port}")

    def receive_udp(self, port: int = 12345):
        # Create a new socket using 'with' to ensure it gets automatically closed
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP) as receive_socket:
            receive_socket.bind((self.ip, port))
            while True:
                print("Listening for incoming UDP packets...")
                packet, _ = receive_socket.recvfrom(65535)  # Receive the packet (maximum UDP size)

                # Decapsulate the IP header
                source_ip, _, data = self.decapsulate_ip(packet)  # Decapsulate the packet to get the IP header and data

                # Extract UDP header fields (bytes 20-21 for source port, bytes 22-23 for destination port)
                source_port = int.from_bytes(packet[20:22], byteorder='big')
                destination_port = int.from_bytes(packet[22:24], byteorder='big')

                # The UDP data starts right after the UDP header, which is 8 bytes
                udp_data = data.decode()  # Assuming the data is UTF-8 encoded

                print(f"Packet received from {source_ip} on port {source_port}: {udp_data}")
                print(f"Destination port: {destination_port}")
        
if __name__ == "__main__":
    s = SocketUDP()
    s.send_udp(("192.168.1.20", 12345), "Hello, UDP!" * 1000)