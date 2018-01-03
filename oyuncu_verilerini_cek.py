import urllib.request as request
from bs4 import BeautifulSoup
import sqlite3
import re

ana_url = 'http://espn.go.com'

takim_url = 'http://espn.go.com/nba/teams'
html_takimlar = request.urlopen(takim_url)

soup_takimlar = BeautifulSoup(html_takimlar)

urls = soup_takimlar.find_all(href=re.compile('/nba/teams/stats'))

takim_urls = [ana_url+url['href'] for url in urls]

takim_adi_sozluk = {'bos':'Boston Celtics',
                  'bkn':'Brooklyn Nets',
                  'nyk':'New York Knicks',
                  'phi':'Philadelphia 76ers',
                  'tor':'Toronto Raptors',
                  'gsw':'Golden State Warriors',
                  'lac':'Los Angeles Clippers',
                  'lal':'Los Angeles Lakers',
                  'pho':'Phoenix Suns',
                  'sac':'Sacramento Kings',
                  'chi':'Chicago Bulls',
                  'cle':'Cleveland Cavaliers',
                  'det':'Detroit Pistons',
                  'ind':'Indiana Pacers',
                  'mil':'Milwaukee Bucks',
                  'dal':'Dallas Mavericks',
                  'hou':'Houston Rockets',
                  'mem':'Memphis Grizzlies',
                  'nor':'New Orleans Pelicans',
                  'sas':'San Antonio Spurs',
                  'atl':'Atlanta Hawks',
                  'cha':'Charlotte Hornets',
                  'mia':'Miami Heat',
                  'orl':'Orlando Magic',
                  'was':'Washington Wizards',
                  'den':'Denver Nuggets',
                  'min':'Minnesota Timberwolves',
                  'okc':'Oklahoma City Thunder',
                  'por':'Portland Trail Blazers',
                  'uth':'Utah Jazz'
                  }

# http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]

for takim in takim_urls:
    takim_kodu = takim[-3:]
    html_takim = request.urlopen(takim)

    soup_takim = BeautifulSoup(html_takim)

    kadro = soup_takim.find_all('tr', class_=re.compile('player'))
    kadro_mac_ist = kadro[:int(len(kadro)/2)]
    
    oyuncular = []
    for satir in kadro_mac_ist:
        for veri in satir:
            oyuncular.append(veri.get_text())
        
    oyuncu_ids = [oyuncu.a['href'].split('/')[7] for oyuncu in kadro_mac_ist]
    
    index = 0
    increment = 0
    for id in oyuncu_ids:
        oyuncular.insert(index + increment, id)
        index = index + 15
        increment = increment + 1
        
    index = 2
    increment = 0
    for id in oyuncu_ids:
        oyuncular.insert(index + increment, takim_adi_sozluk[takim_kodu])
        index = index + 16
        increment = increment + 1

    conn = sqlite3.connect('nba.db')
    c = conn.cursor()

    for satir in chunks(oyuncular,17):
        try:
            c.execute('INSERT INTO oyuncular_ve_istatistikleri VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', satir)
        except:
            pass
        conn.commit()
    conn.close()
