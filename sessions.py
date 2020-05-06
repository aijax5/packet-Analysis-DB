from scapy.all import *
from scapy.layers.http import HTTP
from scapy.layers.inet import IP, TCP

r = rdpcap("src/test.pcap")
# for pkt in r:
#     if TCP in  pkt:
#         print(pkt[IP].src," - ", pkt[TCP].sport)
        # print(pkt[IP].dst," - ", pkt[TCP].dport)

# for session in r.sessions():
#     print(session)
# hostsMac = set()
# for pkt in r:
#     if pkt.haslayer('IP'):
#         # print(pkt.getlayer('ARP').hwsrc)
#         srcIP = pkt.getlayer('IP').src
#         dstIP = pkt.getlayer('IP').dest
#         srcMAC = pkt.getlayer('ARP').hwsrc
#         dstMAC = pkt.getlayer('ARP').hwdst
#         hostsMac.add((srcIP,srcMAC))
#         hostsMac.add((dstIP,dstMAC))

load_layer("http")
packets = sniff(offline="src/test.pcap", session=TCPSession)
# # for pkt in pkts:
# #     print(pkt)



# *****************
# TCP_REVERSE = dict((TCP_SERVICES[k], k) for k in TCP_SERVICES.keys())
# print(TCP_REVERSE)
# for packet in packets:
#     if packet.haslayer('TCP'):
#         p = packet[TCP].sport
#         # if p in TCP_REVERSE:
#         #     print(TCP_REVERSE[packet[TCP].sport])

# ************* HTTP Reqs
for packet in packets:
    if not packet.haslayer('HTTPRequest'):
        continue
    http_layer= packet.getlayer('HTTPRequest').fields 
    ip_layers=packet.getlayer('IP')
    # print(http_layer)
    print(ip_layers.ttl,type(ip_layers.ttl))