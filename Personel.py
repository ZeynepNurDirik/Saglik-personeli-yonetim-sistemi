#Personel classı
class Personel:
    def __init__(self,personel_no,ad,soyad,departman,maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas =maas

        def get_personel_no(self):
            return self.__personel_no

        def get_ad(self):
            return self.__ad

        def get_soyad(self):
            return self.__soyad

        def get_departman(self):
            return self.__departman

        def get_maas(self):
            return self.__maas

        def set_departman(self,departman):
            self.__departman = departman

        def set_maas(self,maas):
            self.__maas = maas

        def __str__(self):
            return "Personel No:{}, Ad:{}, Soyad:{},Departman:{}, Maaş:{}",format(
                self.__personel_no,self.__ad, self.__soyad, self.__departman,self.__maas)



# Bu kısımda get metodları ile bu bilgilere private ulaşım sağladım.
# Her bir özellik için get metodu atadım.
#set metodları ile bu bilgileri güncellenebilir hale getirdim.
#Maas ve departman özelliklerini gerektiğinde değiştirmek için set metodlarını kullandım.
#str metodunda ise nesneyi insan tarafından okunacak hale çevirir.





