# intval = 0
# while True:
#     intval += 1
#     print('sonsuz döngü', intval)



# intval = 10
# while intval != 0:
#     print(intval)
#     intval -= 1



while True:
    ilksinav = float(input('ilk sınav notunuzu girin:'))
    ikincisinav = float(input('ikinci sınav notunuzu girin'))
    ortalama = (ilksinav + ikincisinav) / 2
    print('ortalaman:', ortalama)

    if ortalama > 100:
        print('gerçek notlar giriniz\n')
    elif ortalama < 0:

        print('eksi ortalamaya nasıl ulaştın\n')
    elif ortalama >= 85:
        print('ortalaman çok iyi\n')

    elif ortalama >=70:
        print('ortalaman iyi\n')

    elif ortalama >= 50:
        print('sınıfı geçtin!\n')

    else:
        print('sınıfta kaldın\n')