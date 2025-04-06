import socket
from Phase1.IP.socket_IP import BASE_IP, SocketIP
import time
import threading



class SocketICMP(SocketIP):
    def __init__(self, ip: str = BASE_IP):
        print(f" [ICMP] Binded on {ip} ")
        super().__init__(ip)
        self.protocol = 0x01 # ICMP protocol

    def build_icmp_header(self, icmp_type: int, icmp_code: int, data: str):
        icmp_type_bytes = icmp_type.to_bytes(1, byteorder='big')
        icmp_code_bytes = icmp_code.to_bytes(1, byteorder='big')
        checksum = 0
        checksum_bytes = checksum.to_bytes(2, byteorder='big')
        identifier = (1).to_bytes(2, byteorder='big')
        sequence_number = (1).to_bytes(2, byteorder='big')
        data_bytes = data.encode()
        packet = icmp_type_bytes + icmp_code_bytes + checksum_bytes + identifier + sequence_number + data_bytes
        packet = self.put_checksum(packet, 2, 2)
        return packet
    def send_icmp(self, target_address: tuple[str,int], data: str, icmp_type: int = 8, icmp_code: int = 0):
        icmp_header = self.build_icmp_header(icmp_type, icmp_code, data)
        self.sendall(target_address, icmp_header, self.protocol)
        

    def ping(self, target_ip: str, data: str = "Ping", count: int = 4, timeout: int = 1):
        def listen_for_replies():
            with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
                s.bind((self.ip, 0))
                s.settimeout(timeout)
                try:
                    while True:
                        packet, addr = s.recvfrom(1024)
                        icmp_type = packet[20]
                        icmp_code = packet[21]
                        if addr[0] == target_ip and icmp_type == 0:  # Echo Reply
                            print(f"Reply from {addr[0]}: {data}")
                            break
                except socket.timeout:
                    print("Request timed out.")

        for i in range(count):
            print(f"Pinging {target_ip} with {data}...")
            listener_thread = threading.Thread(target=listen_for_replies, daemon=True)
            listener_thread.start()
            self.send_icmp((target_ip, 0), data, icmp_type=8, icmp_code=0)
            listener_thread.join(timeout + 1)
            time.sleep(1)

if __name__ == "__main__":
    s = SocketICMP()
    s.ping("192.168.1.1", "Ping", count=4, timeout=1)