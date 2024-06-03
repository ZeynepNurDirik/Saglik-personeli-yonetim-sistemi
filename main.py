import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:

        personel1 = Personel(01,"Gizem","Aydın","Resepsiyon",25000)
        personel2 = Personel(02,"Kerem","Yılmaz","Temizlik",20000)
        personel3 = Personel(03,"Melisa","Yıldız","Yönetim",50000)

        print(personel1)
        print(personel2)
        print(personel3)

        doktor1 = Doktor(100,"Sena","Tekin","Göz",85000,
                         "Göz Hastalıkları",2,"Medicana")

        doktor2 = Doktor(101,"Gülnur","Görür","Diş",83000,
                         "Ortodonti",3,"Acıbadem")

        doktor3 = Doktor(102,"Gülsu", "Güzelcan","Fizyoterapi",80000,
                         "Duruş Bozuklukları",2,"Medical Point")

        print(doktor1)
        print(doktor2)
        print(doktor3)

        hemsire1 = Hemsire(200,"Aslı","Kaya","Acil",35000,
                           40,"Sertifika A","Acıbadem")

        hemsire2 = Hemsire(201,"Raziye","Aydın","Acil",38000,
                           36,"Sertifika C","Medical Point")

        hemsire3 = Hemsire(202,"Emine","Tekin","Acil",40000,
                           35,"Sertifika C","Medicana")

        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        hasta1 = Hasta(300,"Damla","Çelik","12.03.2003",
                       "Grip","Serum")

        hasta2 = Hasta(301,"Sude","Yılmaz","08.01.1998",
                       "Yüksek Şeker","İlaç Tedavisi")

        hasta3 = Hasta(302,"Elif","Demir","17.10.2010",
                       "Göz Kuruluğu","İlaç Tedavisi")

        hasta4 = Hasta(303,"Hasan","Dirik","26.06.1977",
                       "Boyun Ağrısı","Egzersiz")

        hasta5 = Hasta(304,"Zeynep","Dirik","06.06.2005",
                       "Grip","İlaç Tedavisi")

        print(hasta1)
        print(hasta2)
        print(hasta3)
        print(hasta4)
        print(hasta5)


        data = {
            "Personel No":[personel1.get_personel_no(),personel2.get_personel_no(),personel3.get_personel_no(),
                           doktor1.get_personel_no(),doktor2.get_personel_no(),doktor3.get_personel_no(),
                           hemsire1.get_personel_no(),hemsire2.get_personel_no(),hemsire3.get_personel_no(),
                           None,None,None,None,None
                           ],
            "Ad":[personel1.get_ad(),personel2.get_ad(),personel3.get_ad(),
                  doktor1.get_ad(),doktor2.get_ad(),doktor3.get_ad(),
                  hemsire1.get_ad(),hemsire2.get_ad(),hemsire3.get_ad(),
                  hasta1.get_ad(),hasta2.get_ad(),hasta3.get_ad(),hasta4.get_ad(),hasta5.get_ad()
                  ],

            "Soyad":[personel1.get_soyad(),personel2.get_soyad(),personel3.get_soyad(),
                     doktor1.get_soyad(),doktor2.get_soyad(),doktor3.get_soyad(),
                     hemsire1.get_soyad(),hemsire2.get_soyad(),hemsire3.get_soyad(),
                     hasta1.get_soyad(),hasta2.get_soyad(),hasta3.get_soyad(),hasta4.get_soyad(),hasta5.get_soyad(),
                     ],

            "Departman":[personel1.get_departman(),personel2.get_departman(),personel3.get_departman(),
                         doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(),
                         hemsire1.get_departman(),hemsire2.get_departman(),hemsire3.get_departman(),
                         None,None,None,None,None
                        ],

            "Maas":[personel1.get_maas(),personel2.get_maas(),personel3.get_maas(),
                    doktor1.get_maas(),doktor2.get_maas(),doktor3.get_maas(),
                    hemsire1.get_maas(),hemsire2.get_maas(),hemsire3.get_maas(),
                    None,None,None,None,None
                    ],

            "Uzmanlık":[None,None,None,
                        doktor1.get_uzmanlik(),doktor2.get_uzmanlik(),doktor3.get_uzmanlik(),
                        None,None,None,
                        None,None,None,None,None,
                        ],

            "Deneyim Yılı":[None,None,None,
                            doktor1.get_deneyim_yili(),doktor2.get_deneyim_yili(),doktor3.get_deneyim_yili(),
                            None,None,None,
                            None,None,None,None,None
                            ],

            "Hastane":[None,None,None,
                       doktor1.get_hastane(),doktor2.get_hastane(),doktor3.get_hastane(),
                       hemsire1.get_hastane(),hemsire2.get_hastane(),hemsire3.get_hastane(),
                       None,None,None,None,None
                       ],

            "Çalışma Saati":[None,None,None,
                             None,None,None,
                             hemsire1.get_calisma_saati(),hemsire2.get_calisma_saati(),hemsire3.get_calisma_saati(),
                             None,None,None,None,None
                             ],

            "Sertifika":[None, None,None,
                         None, None, None,
                         hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(),
                         None, None, None, None, None,
                         ],

            "Hasta No":[None,None,None,
                        None,None,None,
                        None,None,None,
                        hasta1.get_hasta_no(),hasta2.get_hasta_no(),hasta3.get_hasta_no(),hasta4.get_hasta_no(),hasta5.get_hasta_no(),
                        ],

            "Doğum Tarihi":[None,None,None,
                            None,None,None,
                            None,None,None,
                            hasta1.get_dogum_tarihi(),hasta2.get_dogum_tarihi(),hasta3.get_dogum_tarihi(),hasta4.get_dogum_tarihi(),hasta5.get_dogum_tarihi(),
                            ],
            "Hastalık":[None,None,None,
                        None,None,None,
                        None,None,None,
                        hasta1.get_hastalik(),hasta2.get_hastalik(),hasta3.get_hastalik(),hasta4.get_hastalik(),hasta5.get_hastalik(),
                        ],

            "Tedavi":[None,None,None,
                      None,None,None,
                      None,None,None,
                      hasta1.get_tedavi(),hasta2.get_tedavi(),hasta3.get_tedavi(),hasta4.get_tedavi(),hasta5.get_tedavi(),
                      ],

        }

        df = pd.DataFrame(data)











