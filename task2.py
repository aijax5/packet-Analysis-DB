from PacketAnalysisDB.PacketAnalyser import PacketAnalyser
from PacketAnalysisDB.AnalysisDB import AnalysisDB

batch = 10
offset = 1
pa = PacketAnalyser()
db = AnalysisDB(drop=1)

def driver(packetsBatch,db):
    headers = pa.getHTTPHeader(packetsBatch)
    minTTl = min(pa.getMinTTL(packetsBatch))
    macs = pa.getMac(packetsBatch)
    ips = pa.getIPaddr(packetsBatch)
    sess = pa.getSession(packetsBatch)
    tup = (str(minTTl), str(sess if len(sess) else None), str(ips if len(ips) else None), 
           str(macs if len(macs) else None), str(headers if len(headers) else None))
    db.insertTuple(tup)

while offset*batch < pa.numPackets:
    packetsBatch = pa.packets[(offset-1)*batch: offset*batch]
    driver(packetsBatch,db)
    offset += 1

packetsBatch = pa.packets[(offset-1)*batch:]
driver(packetsBatch,db)

if input("\nEnter 'p' to print the tuples in the table:\n") == 'p':
    db.printTable()
# /home/aijax/.vscode/extensions/webrender.synthwave-x-fluoromachine-0.0.11/synthwave-x-fluoromachine.css 