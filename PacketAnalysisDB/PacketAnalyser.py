from scapy.all import *
from scapy.layers.http import HTTP
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import ARP

class PacketAnalyser():
    def __init__(self,intervals =100):
        self.intervals = intervals
        self.packets = rdpcap("src/test.pcap")
        self.numPackets = len(self.packets)
    
    def getHTTPHeader(self,packets):
        """
            returns a list of  HTTP Headers of any possible sessions involved in the 
            packets provided
        """
        headers = []
        for packet in packets:
            if not packet.haslayer('HTTPRequest'):
                headers.append(float('nan'))
                continue
            http_layer= packet.getlayer('HTTPRequest').fields 
            headers.append(http_layer)
        return headers
    
    def getIPaddr(self,packets):
        """
            returns a list of IP addresses involved in the 
            packets provided
        """
        allIPs = set()
        for pkt in packets:
            if pkt.haslayer('IP'):
                # print(pkt.getlayer('ARP').hwsrc)
                srcIP = pkt.getlayer('IP').src
                dstIP = pkt.getlayer('IP').dest
                allIPs.add(srcIP)
                allIPs.add(dstIP)
            
        return allIPs
    
    def getSession(self, packets):
        sessions = []
        for session in packets.sessions():
            sessions.append(session)

        return session

    def getTTL(self, packets):
        allTTL = []
        for packet in packets:
            if IP in packet:
                allTTL.append(packet[IP].ttl)
            else:
                allTTL.append(float('nan'))
        
        return allTTL
    
    def getMac(self, packets) :
        """
            traverses through all packets provided and
            returns a set of tuples (IP, MAC)
        """
        allMac = set()
        for packet in packets:
            if IP in packet:
                allMac.add((packet[IP].src,packet[ARP].hwsrc))
                allMac.add((packet[IP].dst,packet[ARP].hwdst))
        
        return allMac
    