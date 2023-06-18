def a():
    print('meryhabalr')


a()

print('--------------------------------------------------------------------------------------------------')


def hosgeldin(isim):
    print('hoşgeldin {}'.format(isim))
    print('hoşgeldin', isim)


hosgeldin('burak')
hosgeldin('sevgi')

print('--------------------------------------------------------------------------------------------------------')


# def toplama(num1, num2):
#     print('toplam:{}'.format(num1 + num2))


# toplama(4, 5)
# toplama(float(input('ilk sayı:')), float(input('ikinci sayı')))

print('----------------------------------------------------------------------------------------------------------')


def kisi(isim, yas):
    print('isim: {}, yaş:{}'.format(isim, yas))


kisi('mbv', 15)

print('------------------------------------------------------------------------------')


def num_ussu1(sayi1, sayi2):
    print(sayi1**sayi2)


num_ussu1(3, 2)

print('----------------------------------------------------------------------------------------------------------')


def num_ussu2(a1, a2=3):
    print(a1**a2)


num_ussu2(2)

print('----------------------------------------------------------------------------------------------------------')


def num_ussu3(a1, a2=3):
    return a1**a2


print(num_ussu3(3))

print('----------------------------------------------------------------------------------------------------------')


def mod_five(num):
    return num % 5


print(mod_five(19))

print('----------------------------------------------------------------------------------------------------------')


def greater_number(num1, num2):
    '''
        num1 = ilk girilen sayı
        num2 = ikinci girilen sayı
        return = en büyük sayıyı döner
    '''

    if num1 > num2:
        return num1,

    elif num2 > num1:
        return num2
    else:
        return num1


print(greater_number(12, 15))

'''
buraya not alavbilirsin
qwe
qwe
qwe
'''