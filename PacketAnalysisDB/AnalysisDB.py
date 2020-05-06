from PacketAnalysisDB.PacketAnalyser import PacketAnalyser
import sqlite3

class AnalysisDB():
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        create_query = """
        	CREATE TABLE IF NOT EXISTS capture (
                group_no INTEGER PRIMARY_KEY,
                ttl INTEGER,
                sessions TEXT,
                ip_addr TEXT,
                mac_addr TEXT,
                http_headers TEXT
            )
            """
        self.conn.cursor().execute(create_query)
        self.conn.commit()
        self.id = 1
    
    def insertTuple(self, tup):
        insertQuery = "INSERT INTO analysis VALUES (?,?,?,?,?,?)",(self.id)+tup
        conn.commit()
        conn.close()
        self.id += 1
