import sqlite3 as db
from PyQt4 import QtCore, QtGui
import sys

con = db.connect('nba_oyuncu_listesi.db', isolation_level=None)
cur = con.cursor()
cur.execute("SELECT * FROM oyuncular_ve_istatistikleri ORDER BY mbs DESC")
all_data = cur.fetchall()


class UiDialog(object):
    def setupUi(self, datadb):
        datadb.setObjectName("Dialog")
        datadb.resize(404, 304)
        datadb.setWindowTitle("Oyuncu Listesi")
        pencereBoyutu = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        pencereBoyutu.setHorizontalStretch(0)
        pencereBoyutu.setVerticalStretch(0)
        pencereBoyutu.setHeightForWidth(datadb.sizePolicy().hasHeightForWidth())
        datadb.setSizePolicy(pencereBoyutu)
        datadb.setMinimumSize(QtCore.QSize(1111, 501))
        datadb.setMaximumSize(QtCore.QSize(808, 801))
        self.table = QtGui.QTableWidget(datadb)
        self.table.setGeometry(QtCore.QRect(2, 2, 1100, 469))
        self.table.setObjectName("tablo")
        self.goster = QtGui.QPushButton(datadb)
        self.goster.setGeometry(QtCore.QRect(350, 470, 400, 31))
        self.goster.setObjectName("goster")
        self.goster.setText("Oyuncu Listesini Göster")
        QtCore.QObject.connect(self.goster, QtCore.SIGNAL("clicked()"), self.populate)
        QtCore.QMetaObject.connectSlotsByName(datadb)
        

    def populate(self):
        self.table.blockSignals(True)
        self.table.setRowCount(len(all_data))
        self.table.setColumnCount(17)
        self.table.setHorizontalHeaderLabels(['id', 'Adı', 'Takım Adı', 'Oynadığı Maç',
                                              'İlk Beş Başladığı', 'Ortalama Dakika', 'MB Sayı Ort',
                                              'MB Hücum Rib', 'MB Savunma Rib', 'MB Rib',
                                              'MB Assist', 'MB Top Çalma', 'MB Blok', 'MB Top Kaybı',
                                              'MB Foul', 'A/Tk Oranı', 'PER'])
        for i, item in enumerate(all_data):
            idd = QtGui.QTableWidgetItem(str(item[0]))
            adi = QtGui.QTableWidgetItem(str(item[1]))
            takim_adi = QtGui.QTableWidgetItem(str(item[2]))
            oynadigi_mac_sayisi = QtGui.QTableWidgetItem(str(item[3]))
            ilk_bes = QtGui.QTableWidgetItem(str(item[4]))
            dk = QtGui.QTableWidgetItem(str(item[5]))
            mbs = QtGui.QTableWidgetItem(str(item[6]))
            offr = QtGui.QTableWidgetItem(str(item[7]))
            defr = QtGui.QTableWidgetItem(str(item[8]))
            mbr = QtGui.QTableWidgetItem(str(item[9]))
            mba = QtGui.QTableWidgetItem(str(item[10]))
            mbtc = QtGui.QTableWidgetItem(str(item[11]))
            mbb = QtGui.QTableWidgetItem(str(item[12]))
            mbtk = QtGui.QTableWidgetItem(str(item[13]))
            mbf = QtGui.QTableWidgetItem(str(item[14]))
            a_to = QtGui.QTableWidgetItem(str(item[15]))
            per = QtGui.QTableWidgetItem(str(item[16]))
            

            
            self.table.setItem(i, 0, idd)
            self.table.setItem(i, 1, adi)
            self.table.setItem(i, 2, takim_adi)
            self.table.setItem(i, 3, oynadigi_mac_sayisi)
            self.table.setItem(i, 4, ilk_bes)
            self.table.setItem(i, 5, dk)
            self.table.setItem(i, 6, mbs)
            self.table.setItem(i, 7, offr)
            self.table.setItem(i, 8, defr)
            self.table.setItem(i, 9, mbr)
            self.table.setItem(i, 10, mba)
            self.table.setItem(i, 11, mbtc)
            self.table.setItem(i, 12, mbb)
            self.table.setItem(i, 13, mbtk)
            self.table.setItem(i, 14, mbf)
            self.table.setItem(i, 15, a_to)
            self.table.setItem(i, 16, per)
            
        self.table.blockSignals(False)
        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_conf = QtGui.QDialog()
    ui = UiDialog()
    ui.setupUi(main_conf)
    main_conf.show()
    ret = app.exec_()
    sys.exit(ret)
