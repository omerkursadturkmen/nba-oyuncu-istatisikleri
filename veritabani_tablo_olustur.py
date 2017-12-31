import sqlite3

conn = sqlite3.connect('nba_oyuncu_listesi.db')

conn.execute('''CREATE TABLE oyuncular_ve_istatistikleri ( "id" INTEGER PRIMARY KEY NOT NULL,
"adi" TEXT NOT NULL, "takim_adi" TEXT NOT NULL,
"oynadigi_mac_sayisi" INTEGER NOT NULL, "ilk_bes" INTEGER NOT NULL, "DK" REAL NOT NULL,
"MBS" REAL NOT NULL, "OFFR" REAL NOT NULL, "DEFR" REAL NOT NULL, "MBR" REAL NOT NULL, "MBA" REAL NOT NULL, "MBTÇ" REAL NOT NULL,
"MBB" REAL NOT NULL, "MBTK" REAL NOT NULL, "MBF" REAL NOT NULL, "A/TO" REAL NOT NULL, "PER" REAL NOT NULL)''')

conn.close()
