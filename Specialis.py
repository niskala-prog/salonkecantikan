import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Specialis:

    def __init__(self):
        self.__id_specialis=None
        self.__kode_specialis=None
        self.__nama_specialis=None
        self.__kategori=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "kode_specialis:" + self.__kode_specialis + "\n" + "nama_specialis:" + self.__nama_specialis + "\n"
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id_specialis(self):
        return self.__id_specialis

    @property
    def kode_specialis(self):
        return self.__kode_specialis

    @kode_specialis.setter
    def kode_specialis(self, value):
        self.__kode_specialis = value

    @property
    def nama_specialis(self):
        return self.__nama_specialis

    @nama_specialis.setter
    def nama_specialis(self, value):
        self.__nama_specialis = value


    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_specialis, self.__nama_specialis)
        sql="INSERT INTO kategori (kode_specialis, nama_specialis__nama_specialis) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id_specialis):
        self.conn = mydb()
        val = (self.__kode_specialis, self.__nama_specialis, id_specialis)
        sql="UPDATE kategori SET kode_specialis = %s, nama_specialis= %s, WHERE id_specialiskat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode_specialis(self, kode_specialis):
        self.conn = mydb()
        val = (self.__nama_specialis, kode_specialis)
        sql="UPDATE kategori SET nama_specialis__nama_specialis = %s, jk=%s WHERE kode_specialis=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id_specialis):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE id_specialismhs='" + str(id_specialis) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykode_specialis(self, kode_specialis):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE kode_specialis='" + str(kode_specialis) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByid_specialis(self, id_specialis):
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE id_specialismhs='" + str(id_specialis) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_specialis = self.result[1]
        self.__nama_specialis = self.result[2]
        self.__jk = self.result[3]
        self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getBykode_specialis(self, kode_specialis):
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE kode_specialis='" + str(kode_specialis) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_specialis = self.result[1]
            self.__nama_specialis = self.result[2]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_specialis = ''
            self.__nama_specialis = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM kategori limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
