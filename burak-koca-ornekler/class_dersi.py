class Ogrenci:
    def __init__(self, ad, ilksinav, ikincisinav):
        self.ad = ad
        self.ilksinav = ilksinav
        self.ikincisinav = ikincisinav
        print('{} öğrencisi listeye eklendi'.format(ad))

    def not_hesaplama(self):
        return (self.ilksinav + self.ikincisinav) / 2

    def ekrana_yazdir(self):
        print('\n{} adlı öğrencinin ilk sınav notu: {}, ikinci sınav notu {}, dönem sonu not ortalaması: {}'
        .format(self.ad, self.ilksinav, self.ikincisinav, Ogrenci.not_hesaplama(self)))

    def __repr__(self):
        return 'merhaba ' + self.ad

    def __add__(self, other):
        return 'merhaba ' + other



ogr1 = Ogrenci('burak', 95, 96, )
ogr2 = Ogrenci('fatik', 85, 90)
ogr3 = Ogrenci('ahme', 45, 50)

ogr1.ekrana_yazdir()
ogr2.ekrana_yazdir()
ogr3.ekrana_yazdir()

print('----------------------------------------------------------------------------------------------------------')

print(ogr1)

print('------------------------------------------------------------------------------------------------------------')
print(ogr1 + 'python')
