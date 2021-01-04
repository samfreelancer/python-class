import pymysql

class Database:
    hostname = 'localhost'
    username = 'root'
    password = 'P@ssw0rd'
    database = 'sample'
    conn = ''
    obj = ''
    def __init__(self):
        self.conn = pymysql.connect(host=self.hostname, user=self.username, passwd=self.password, db=self.database)

    @staticmethod
    def getObject():
        if Database.obj == '':
            obj = Database()
        return obj

    def getConnection(self):
        if self.conn == '':
            self.__init__()
        return self.conn

    def getCursor(self):
        return self.conn.cursor()

    def getData(self, query, obj = ''):
        cursor = self.getCursor()
        cursor.execute(query)
        if obj != '':
            obj.showData(cursor.fetchall())
        else:
            return cursor.fetchall()