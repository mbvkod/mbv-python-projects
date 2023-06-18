def toplama(num1, num2):
    print(num1 + num2)


toplama(3, 5)
# toplama(2, 4, 5)

print('---------------------------------------------------------------------------------------------------------')


def func(*value):
    print(type(value))


func(12, 32)
func(12390, 'qwsmdkşad')

print('---------------------------------------------------------------------------------------------------')


def function(*value):
    for a in value:
        print(a)
        print(type(a))


function('qwdköl', 123.2, 123123, 'wdsrfl')

print('----------------------------------------------------------------------------------------------------')


def toplam(*numbers):
    toplamval = 0
    for num in numbers:
        toplamval += num
    print(toplamval)


toplam(12, 5, 3)
toplam(12, 4, 2, 4, 2)

print('---------------------------------------------------------------------------------------------------')


def ortalama(*numbers):
    toplamval = 0
    for num in numbers:
        toplamval += num
    uzunluk = len(numbers)
    sonuc = toplamval / uzunluk
    print(sonuc)


ortalama(3, 5, 7)

print('---------------------------------------------------------------------------------------------------')


def number12(**details):
    for personel in details.keys():
        print(personel)
    print('')
    for personel in details.values():
        print(personel)
    print('')
    for personel in details.items():
        print(personel)
    print('')
    for key, val in details.items():
        print(key, val)


number12(isim='burak', yaş=15, meslek='öğrenci')

print('----------------------------------------------------------------------------------------------------')


def alan(**values):
    if 'en' not in values:
        print('en parametresi boş bırakılamaz')
    elif 'boy' not in values:
        print('boy parametresi boş bırakılaamz')
    else:
        print(values['en'] * values['boy'])


alan(renk='siyah', en=12, boy=3)

print('------------------------------------------------------------------------')


def argkwarg(val, *arg, **kwarg,):
    print(val)
    print(arg)
    print(kwarg)


argkwarg(12, 1234, 'wefrö', 123, 'dfıkolş', isim='ahme', yaş=15)
