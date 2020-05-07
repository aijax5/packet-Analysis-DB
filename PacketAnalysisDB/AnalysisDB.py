from PacketAnalysisDB.PacketAnalyser import PacketAnalyser
import sqlite3


class AnalysisDB():
    def __init__(self, drop=0):
        self.conn = sqlite3.connect('database.db')
        if drop:
            self.dropTable()

        create_query = """
        	CREATE TABLE IF NOT EXISTS capture (
                sid INTEGER PRIMARY_KEY,
                min_ttl INTEGER,
                sessions TEXT,
                ip_ports TEXT,
                mac_addr TEXT,
                http_headers TEXT
            )
            """
        self.conn.cursor().execute(create_query)
        self.conn.commit()
        self.id = 1

    def insertTuple(self, tup):
        self.conn.cursor().execute("INSERT INTO capture VALUES (?,?,?,?,?,?)", (self.id,)+tup)
        self.conn.commit()
        self.id += 1

    def dropTable(self):
        self.conn.cursor().execute("DROP TABLE IF EXISTS capture")
        self.conn.commit()

    def printTable(self):
        res = self.conn.cursor().execute("SELECT * FROM capture")
        for t in res:
            print(t)
            print("\n---------------------    *     -----------------------    *    -----------------------    *   --------\n")
        self.conn.commit()
        self.conn.close()
