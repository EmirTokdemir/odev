import buyukveriA as baslatma
import buyukveriB as crud
import lib as k

def geral():
    k.os.system('cls')

def tGetir():
    yukle = "SELECT * FROM kab"
    getir =crud.imlec.execute(yukle)
    print("|[ID]|[  AD  ]|[YAŞ]|")
    for veri in getir:
        print(
            "|",veri[0],
            "|",veri[1],
            "|",veri[2],
            "|"
            )
    Menu()

def tIsle(ad,yas):
    crud.imlec.execute("INSERT OR REPLACE INTO kab VALUES(null,?,?);",(ad,yas,))
    crud.vt.commit()
    geral()
    print("Veriler işlendi : \n","Ad: ",ad," \n","Yas: ",yas)
    Menu()

def tKaldir(id):
    kaldir = "DELETE FROM kab WHERE id=?"
    crud.imlec.execute(kaldir,(id,))
    crud.vt.commit()
    print("Veri tablodan kaldırıldı \n","Kaldırılan veri Id:",id)
    Menu()


secenekler = ["Tablo Getir","Tabloya İşle","Tablo'dan Kaldır","Çıkış"]

def Menu():
    i = 0
    print("App dahilinde yapılabilecekler listesi:")
    for islemler in secenekler:
        i+=1
        print(i,".",islemler)
    print()
    secim = input("Yapmak istediğiniz işin No'sunu girin: ")
    secim = int(secim)

    if secim == 1:
        geral()
        tGetir()


    elif secim == 2:
        geral()
        print("Eklenilecek Kişinin Adı ve Yaşını giriniz")
        AD = input("Ad:")
        YAS = input("Yaş:")
        tIsle(AD,YAS)
    

    elif secim == 3:
        geral()
        print("geralinecek verinin ID sini giriniz")
        ID = input("ID:")
        tKaldir(ID)

    elif secim==4:
        geral()
        print("Çıkış yapıldı")
        exit()
    
    else :
        print("Lütfen geçerli bir seçenek giriniz")
        Menu()
