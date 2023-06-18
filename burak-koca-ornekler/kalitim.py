class Insan:
    def __init__(self, gelenad, gelensoyad):
        self.ad = gelenad
        self.soyad = gelensoyad

    def bilgileri_yazdir(self):
        return ('''
-----kişi bilgileri-----
ad: {}
soyad: {}
''').format(self.ad, self.soyad)


# ---------------------------------------------------------------------------------------------------------------


class Ogrenci(Insan):
    def __init__(self, gelenad, gelensoyad, gelennotu):
        Insan.__init__(self, gelenad, gelensoyad)
        self.notu = gelennotu


    def bilgileri_yazdir(self):
        return Insan.bilgileri_yazdir(self) + 'notu: {}'.format(self.notu)


# ---------------------------------------------------------------------------------------------------------------



class Ogretmen(Insan):
    def __init__(self, gelenad, gelensoyad, gelenmaas):
        Insan.__init__(self, gelenad, gelensoyad)
        self.maas = gelenmaas

    def bilgileri_yazdir(self):
        return Insan.bilgileri_yazdir(self) + 'maaşı: {}'.format(self.maas)

# ---------------------------------------------------------------------------------------------------------------


insan1 = Insan('Burak', 'Velioğlu')
ogrenci1 = Ogrenci('Burak', 'Velioğlu', 12)
ogretmen1 = Ogretmen('fatma', 'kılıç', 3000)


print(insan1.bilgileri_yazdir())
print(ogrenci1.bilgileri_yazdir())
print(ogretmen1.bilgileri_yazdir())
