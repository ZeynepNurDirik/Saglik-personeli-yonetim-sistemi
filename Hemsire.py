#Hemşire classı

from Personel import Personel

class Hemsire(Personel):
    def __init__(self,personel_no,ad,soyad,departman,maas,calisma_saati ,sertifika ,hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane


    def get_calisma_saati(self):
        return self.__calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def get_hastane(self):
        return self.__hastane

    def set_calisma_saati(self,calisma_saati):
        self.__calisma_saati = calisma_saati

    def set_sertifika(self,sertifika):
        self.__sertifika = sertifika

    def set_hastane(self,hastane):
        self.__hastane =hastane

    def maas_artirma(self, oran):
        self.set_maas(self.get_maas()* (1+oran))

    def __str__(self):
        return "{}, Calisma Saati:{}, Sertifika: {}, Hastane:{}".format(
            super().__str__(), self.__calisma_saati , self.__sertifika, self.__hastane
        )
#Hemşire sınıfı personel sınıfından miras alır ve bu özelliklere ek calisma saati, sertifika,hastane bilgilerini ekler.
# __init__metpdu hemsire sınıfının yapıcı metodudur.bu metod nesnenin başlangıç değerlerini belirler.
#super().__init__ ile hemsire sinifi personel sinifinin tüm özelliklerine sahip olur.
#def ve set metodlarını diğer sınıflarda olduğu gibi ozelliklere dışarıdan güvenli erişim ve değiştirilebilir hale getirdim.
#def __str__ hemşirenin tüm bilgilerini string olarak döndürür.