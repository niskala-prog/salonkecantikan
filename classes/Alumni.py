from config.db import DBConnection as mydb

class Alumni:

    def __init__(self):
        self.__id=None
        self.__kode_alumni=None
        self.__nama=None
        self.__jk=None
        self.__tahun_lulus=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "Kode Alumni:" + self.__kode_alumni + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Tahun Lulus:" + self.__tahun_lulus
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def kode_alumni(self):
        return self.__kode_alumni

    @kode_alumni.setter
    def kode_alumni(self, value):
        self.__kode_alumni = value

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

    @property
    def tahun_lulus(self):
        return self.__tahun_lulus

    @tahun_lulus.setter
    def tahun_lulus(self, value):
        self.__tahun_lulus = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_alumni, self.__nama, self.__jk, self.__tahun_lulus)
        sql="INSERT INTO alumni (kode_alumni, nama, jk, tahun_lulus) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_alumni, self.__nama, self.__jk, self.__tahun_lulus, id)
        sql="UPDATE alumni SET kode_alumni = %s, nama = %s, jk=%s, tahun_lulus=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode_alumni(self, kode_alumni):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__tahun_lulus, kode_alumni)
        sql="UPDATE alumni SET nama=%s, jk=%s, tahun_lulus=%s WHERE kode_alumni=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM alumni WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykode_alumni(self, kode_alumni):
        self.conn = mydb()
        sql="DELETE FROM alumni WHERE kode_alumni='" + str(kode_alumni) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM alumni WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_alumni = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__tahun_lulus = self.result[4]
        self.conn.disconnect
        return self.result

    def getBykode_alumni(self, kode_alumni):
        self.conn = mydb()
        sql="SELECT * FROM alumni WHERE kode_alumni='" + str(kode_alumni) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_alumni = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__tahun_lulus = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_alumni = ''
            self.__nama = ''
            self.__jk = ''
            self.__tahun_lulus = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM alumni limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
