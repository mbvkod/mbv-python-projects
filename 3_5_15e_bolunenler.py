x = 0
while 1 > x:
    sayi = float(input('sayı giriniz: '))

    if sayi % 15 == 0:
        print('15e bolunur')

    elif sayi % 3 == 0:
        print('3e bolunur')

    elif sayi % 5 == 0:
        print('sayı 5e bölünür')

    else:
        print('sayı 3e yada 5e bölünmez')
    print('')

