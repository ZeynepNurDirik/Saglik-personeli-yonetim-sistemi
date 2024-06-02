from Personel import Personel

class Doktor(Personel):
    def __init__(self,personel_no,ad,soyad,departman,maas,uzmanlık,deneyim_yili,hastane):
        super().__init__(personel_no,ad,soyad,departman,maas)
        self.__uzmanlık = uzmanlık
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def get_uzmanlik(self):
        return.__uzmanlik

    def get_deneyim_yili(self):
        return.__deneyim_yili

    def get_hastane(self):
        return.__hastane

    def set_deneyim_yili(self):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self):
        self.__hastane = hastane

    def set_maas_artirma(self,oran):
        self.set_maas(self.get_maas()*(1 + oran))







