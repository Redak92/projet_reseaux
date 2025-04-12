from scapy.all import ICMP, Raw, send
from IP import IPSocket



class ICMPSocket(IPSocket):
    def __init__(self, src_ip=None):
        super().__init__(src_ip)
        self.protocol = 1
        self.id = 1
        self.seq = 1

    def encapsulate_icmp(self, icmp_type: int, icmp_code: int,  data: bytes):
        packet = ICMP(
            type=icmp_type,
            code=icmp_code,
            id=self.id,
            seq=self.seq
        ) / Raw(load=data)
        packet.chksum = 0
        checksum_value = self.checksum(bytes(packet))
        packet.chksum = checksum_value
        return packet
    
    def send_icmp(self, destination: str,ptype: int = 8, code: int = 0 ,data: bytes="abcdefghijklmnopqrstuvwxyz"):
        packet = self.encapsulate_icmp(ptype, code, data)
        packet.show()
        self.send_ip(destination, bytes(packet), self.protocol)


if __name__ == "__main__":
    s = ICMPSocket("127.0.0.1")
    s.send_icmp("127.0.0.1")

        


