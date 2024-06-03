# Hasta classı

class Hasta:
    def __init__(self,hasta_no,ad,soyad,dogum_tarihi,hastalik,tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def get_hasta_no(self):
        return self.__hasta_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik

    def get_tedavi(self):
        return self.__tedavi

    def set_hastalik(self,hastalik):
        self.__hastalik = hastalik

    def set_tedavi(self,tedavi):
        self.__tedavi = tedavi

    def tedavi_suresi_hesapla(self):
        tedavi_suresi= len(self.__tedavi)
        return tedavi_suresi

    def __str__(self):
        return "{}, Hasta No:{}, Ad:{},Soyad:{},Dogum Tarihi:{},Hastalık:{}, Tedavi:{}",format(
            super().__str__(),self.__self.__hasta_no,self.__ad,self.__soyad,self.__dogum_tarihi,
            self.__hastalik,self.__tedavi
        )

#Hasta classı hasta no,ad,soyad,dogum tarihi,hastalık,tedavi bilgilerini içerir.
#self.__ kullanımı sınıf içindeki özellkleri özel yapmak ve dış erişimi guvenli hale getirmek için kullanılır.
