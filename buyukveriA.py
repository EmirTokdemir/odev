from lib import sql
from buyukveriB import terlık 
from buyukveriB import gelme

db_adi= terlık

def basla():
    if db_adi:
     print("Bağlantı Sağlanıldı")
     gelme()
     print("Tablo oluşturuldu/Tabloya Bağlanıldı")
    else :
     print("Veri Tabanına ulaşılamıyor")
