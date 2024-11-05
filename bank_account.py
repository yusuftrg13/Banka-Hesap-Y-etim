"""
Banka Hesap Yönetim Sistemi:
Adımlar:
Hesap:Temel bir banka hesabıyla ilgili işlem ve bilgileri tanımlıcaz
Bank:Hesap yönetiminden sorumlu olacak hesap listele yazdır gibi
"""

class Hesap:
    def __init__(self,hesapno,hesapsahip):
        self.hesapno=hesapno
        self.hesapsahip=hesapsahip
        self.bakiye=0

    def paraYatir(self,miktar):
        if miktar>0:
            self.bakiye += miktar
            print(f"{miktar} TL para yatırıldı.Yeni bakiyeniz:{self.bakiye}")
        else:
            print("Yatıracağınız tutar sıfırdan büyük olmalı")


    def paraCek(self,miktar):
        if 0<miktar<self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} Tl para çekildi.GÜncel bakiyeniz:{self.bakiye}")
        else:
            print("Yetersiz bakiye vea geçersiz tutar")

    def bakiyeGoster(self):
        return self.bakiye
    




class Bank:
    def __init__(self):
        self.hesap=[]


    def hesapOlustur(self,hesapno,hesapsahip):
        yenihesap=Hesap(hesapno,hesapsahip)
        self.hesap.append(yenihesap)
        print(f"{hesapsahip} adına hesap olusturuldu")


    def hesapGöster(self,hesapno):
        for hesap in self.hesap:
            if hesap.hesapno==hesapno:
                return hesap
            print("Hesap bulunamadı")
            return None


#Banka nesnei oluşturalım
bank=Bank()

#Hesap oluşturalım
bank.hesapOlustur("1001","Ali Veli")

hesap1=bank.hesapGöster("1001")
hesap2=Hesap("1002","Ayşe Fatma")
hesap2.paraYatir(2500)
