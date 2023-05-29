import sqlite3, os, time

class Main:
    def __init__(self):
        os.system("cls")
        while True:
            print("Otomasyon Sistemi".center(30,"-"))
            print("1) Yonetici İşlemleri\n2) Kitap İşlemleri")
            sec = int(input("Seçiminiz: ")) 
            if sec == 1:
                yonetici1 = Yonetici()
                yonetici1
            elif sec == 2:
                kitaplik = Kutuphane()
                kitaplik
            else:
                print("Hatalı Seçim") 
        
                      
class Yonetici:
    
    def __init__(self):
        os.system("cls")
        while True:
            print("Yonetici Penceresi".center(30,"-"))
            print("1) Ekle\n2) Listele")
            sec = int(input("Seçiminiz: "))
            
            if sec == 1:
                self.ekle()
            elif sec == 2:
                self.listele()
            else:
                print("Hatalı Seçim")
    
    def ekle(self):
        os.system("cls")
        try:
            self.sicilNo = int(input("Sicil No: "))
            self.adisoyadi = input("Adı Soyadi: ")
            self.maas = int(input("Maaş Bilgisi: "))
            self.eposta = input("Eposta Bilgisi: ")
            
            baglan = self.baglanti()
            imlec =  baglan.cursor()
            imlec.execute(f"insert into tbl_yonetici values({self.sicilNo}, '{self.adisoyadi}', {self.maas}, '{self.eposta}')")
            baglan.commit()
            time.sleep(1)
            print("\nBilgiler Kaydedilmiştir")
            time.sleep(1)                        
        except Exception as hata:
            print(hata)
            
    def listele(self):
        os.system("cls")
        try:
            baglan = self.baglanti()
            imlec =  baglan.cursor()
            imlec.execute("select * from tbl_yonetici")
            print("    Bilgiler Listelenmiştir")
            for kayit in imlec.fetchall():
                print(f"""
    ...SicilNo..    ...Adı Soyadı...     ...Maaş...     ......E-Posta.....
    \t{kayit[0]}\t\t{kayit[1]}\t\t{kayit[2]}\t\t{kayit[3]}""")
            
            time.sleep(3)
            os.system("cls")
        except Exception as hata:
            print(hata)
        
        
    def baglanti(self):
        with sqlite3.connect("arsiv.db") as baglan:
            imlec = baglan.cursor()
            imlec.execute("create table if not exists tbl_yonetici(sicilNo INT, adiSoyadi TEXT, maas INT, eposta TEXT)")
            return baglan    
        

class Kutuphane:
    def __init__(self):
        os.system("cls")
        while True:
            print("Kitaplık Penceresi".center(30,"-"))
            print("1) Ekle\n2) Listele\n3) Sil\n4) Güncelle\n5) Ana Menu")
            sec = int(input("Seçiminiz: "))
            
            if sec == 1:
                self.ekle()
            elif sec == 2:
                self.listele()
            elif sec == 3:
                self.sil()
            elif sec == 4:
                self.guncelle()
            elif sec == 5:
                return Main()  # anasayfaya dön
            else:
                print("Hatalı Seçim")
    
    def baglanti(self):
        with sqlite3.connect("arsiv.db") as baglan:
            imlec = baglan.cursor()
            imlec.execute("create table if not exists tbl_kitaplik(kitapNo INT, adi TEXT, fiyat INT, yazar TEXT)")
            return baglan 

    def listele(self):
        os.system("cls")
        try:
            baglan = self.baglanti()
            imlec =  baglan.cursor()
            imlec.execute("select * from tbl_kitaplik")
            print("    Bilgiler Listelenmiştir")
            for kayit in imlec.fetchall():
                print(f"""
    ...KitapNo...    ...Adı...     ...Fiyat...     ......Yazar.....
    \t{kayit[0]}\t\t{kayit[1]}\t\t{kayit[2]}\t\t{kayit[3]}""")
                
            
            time.sleep(3)
            
        except Exception as hata:
            print(hata)

    def sil(self):
        self.listele()
        try:
            silinecekID = int(input("Aranan Kitap ID: "))
            baglan = self.baglanti()
            imlec = baglan.cursor()
            imlec.execute("delete from tbl_kitaplik where kitapNo={}".format(silinecekID))
            baglan.commit()
            time.sleep(1)
            print(silinecekID,"Kitabı Silindi")
            
        except Exception as hata:
            print(hata)
            
    def guncelle(self):
        self.sil()
        self.ekle()
        
    def ekle(self):
        os.system("cls")
        try:
            self.kitapNo = int(input("Kitap No: "))
            self.adi = input("Adı: ")
            self.fiyat = int(input("Fiyat: "))
            self.yazar = input("Yazar: ")
            
            baglan = self.baglanti()
            imlec = baglan.cursor()
            imlec.execute(f"insert into tbl_kitaplik values({self.kitapNo}, '{self.adi}', {self.fiyat}, '{self.yazar}')")
            baglan.commit()
            time.sleep(1)
            print("Bilgiler Kaydedilmiştir")
            time.sleep(3)
            os.system("cls")
        except Exception as hata:
            print(hata)
        
main = Main()
main