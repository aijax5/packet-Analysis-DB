from PacketAnalysisDB.PacketAnalyser import PacketAnalyser

pa = PacketAnalyser()

pkts = pa.packets

print("ALL HTTP HEADERS \n",pa.getHTTPHeader(pkts))
print("ALL MIN TTL:\n",min(pa.getMinTTL(pkts)))
print("ALL MAC ADDRESS with IP:\n",pa.getMac(pkts))
print("ALL PORTS with IP\n",pa.getIPaddr(pkts))
print("ALL SESSIONS\n",pa.getSession(pkts))
#please refer task1.txt for description