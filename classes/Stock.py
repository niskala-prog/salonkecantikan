from config.db import DBConnection as mydb

class Dosen:

    def __init__(self):
        self.__id=None
        self.__kode_dosen=None
        self.__nama=None
        self.__jk=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "kode_dosen:" + self.__kode_dosen + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def kode_dosen(self):
        return self.__kode_dosen

    @kode_dosen.setter
    def kode_dosen(self, value):
        self.__kode_dosen = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_dosen, self.__nama, self.__jk)
        sql="INSERT INTO dosen (kode_dosen, nama, jk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_dosen, self.__nama, self.__jk, id)
        sql="UPDATE dosen SET kode_dosen = %s, nama = %s, jk=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode_dosen(self, kode_dosen):
        self.conn = mydb()
        val = (self.__nama, self.__jk, kode_dosen)
        sql="UPDATE dosen SET nama = %s, jk=%s WHERE kode_dosen=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykode_dosen(self, kode_dosen):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE kode_dosen='" + str(kode_dosen) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_dosen = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getBykode_dosen(self, kode_dosen):
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE kode_dosen='" + str(kode_dosen) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_dosen = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_dosen = ''
            self.__nama = ''
            self.__jk = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dosen limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
