from scapy.all import UDP, Raw, send, IP
from .IP import IPSocket

class UDPSocket(IPSocket):
    def __init__(self, src_ip=None, src_port=0):
        super().__init__(src_ip)
        self.src_port = src_port
        self.protocol = 17

    def encapsulate_udp(self, dest_port: int, data: bytes):
        total_length = len(data) + 8
        packet = UDP(
            sport=self.src_port,
            dport=dest_port,
            len=total_length,
            chksum=0
        ) / Raw(load=data)
        
        return packet
    

    

    def sendto(self,data: bytes, dest: tuple[str, int]):
        destination, dest_port = dest
        packet = self.encapsulate_udp(dest_port, data)
        send(IP(dst=destination, src=self.src_ip, id=self.packet_number) / packet, verbose=False)
        self.packet_number += 1

    def receive_udp(self, interface: str = "lo"):
        self.start_receiver(interface, filtre=f"udp and port {self.src_port}")

        while True:
            if interface == "lo":
                self.packet_queue.get()
            packet = self.packet_queue.get()

            if UDP in packet and packet[UDP].dport == self.src_port:
                data = bytes(packet[UDP].payload)
                yield data, (packet[UDP].sport, packet[IP].src)


if __name__ == "__main__":
    if input("Start receiver? (y/n): ").lower() == 'y':
        s = UDPSocket("192.168.10.2", 12345)
        for data, addr in s.receive_udp("veth1"):
            print(f"Received from {addr}: {data}")
    else:
        s = UDPSocket("192.168.10.1", 8081)
        s.send_udp("192.168.10.2", 8081, b"Hello, UDP!")