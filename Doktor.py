from Personel import Personel

class Doktor(Personel):
    def __init__(self,personel_no,ad,soyad,departman,maas,uzmanlık,deneyim_yili,hastane):
        super().__init__(personel_no,ad,soyad,departman,maas)
        self.__uzmanlık = uzmanlık
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane

    def set_deneyim_yili(self):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self):
        self.__hastane = hastane

    def set_maas_artirma(self,oran):
        self.set_maas(self.get_maas()*(1 + oran))

    def __str__(self):
        return "{}, Uzmanlık:{}, Deneyim Yılı:{}, Hastane: {}".format(
            super().__str__(), self.__uzmanlik , self.__deneyim_yili , self.__hastane
        )

#Doktor classımda personel classından kalıtım aldım.
#Ek olarak uzmanlık deneyim yılı ve hastane bilgilerini get metoduyla bir sınıfın özel bilgilerine dışarıdan güvenli erişim sağladım.
#set metodları sınıfın içindeki özelliklerin dışarıdan güvenli bir şekilde değiştirmek için kulanılır.
#def __str__ metodu print ifadesi ile içindeki bilgileri ekrana yazdırır.







