class Calisan:
    def __init__(self):
        self.calisanBilgi()
    
    def calisanBilgi(self):
        self.adi = input("Çalışan Adı: ")
        self.soyadi = input("Çalışan Soyadi: ")
        self.yas = int(input("Çalışan Yaş: "))
        # self.isTecrubesi()
        # print(self.tecrubeler)

    def isTecrubesi(self):
        self.tecrubeler = []
        self.adet = int(input("Kaç İş Başvurusu Var: "))
        for i in range(self.adet):
            self.isyeriAdi = input("İs Yeri Adi: ")
            self.gorevi = input("Görevi: ")
            self.kacYil = int(input("Kaç Yıl Çalıştınız: "))
            self.ayrilmaSebebi = input("Ayrılma Sebebi: ")
            self.bilgiler = self.isyeriAdi + " " + self.gorevi + " " + str(self.kacYil) + " " + self.ayrilmaSebebi
            self.tecrubeler.append(self.bilgiler)


class Amir:
    def __init__(self):
        self.adres = input("Adres gir:")
        self.eposta = input("Eposta: ")


class Yazilimci(Amir):
    def __init__(self):
        super().__init__()
        self.programDilleri()
    
    def programDilleri(self):
        self.programlar = list()
        self.adet = int(input("Kaç Yazılım Dili Biliyorsunuz: "))
        for _ in range(self.adet):
            self.programAdi = input("Yazılım Adi: ")
            self.tecrube = int(input("Kaç Yıllık Tecrubeniz Var: "))
            self.maas = int(input("Maaş Beklentisi: "))
            self.bilgiler = self.programAdi + " " + str(self.tecrube) + " " + str(self.maas)
            self.programlar.append(self.bilgiler)
        print(self.programlar)
            

calisan1 = Calisan()
yazilimci1 = Yazilimci()

yazilimci1