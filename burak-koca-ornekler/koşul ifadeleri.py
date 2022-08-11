# intval = 5
# print('değişkenin ilk hali:', intval)

# if True:
#     intval = intval + 1
#     print('değişkene 1 eklendi')

# print('değişkenin son hali:', intval)


intval1 = 20
intval2 = 20

# if intval1 > intval2:
#     print('ilk değişkenim ikincisinden daha büyüktür')

# if intval2 > intval1:
#      print('ikinci değişkenim daha büyüktür')


# if intval1  > intval2:
#     print('birinci değişkenim daha büyüktür')

# elif intval2 >intval1:
#     print('ikinci değişken daha büyüktür')

# elif intval1 == intval2:
#     print('değişkenler birbirine eşittir')


# if intval1  > intval2:
#     print('birinci değişkenim daha büyüktür')

# elif intval2 >intval1:
#     print('ikinci değişken daha büyüktür')

# else intval1 == intval2:
#     print('değişkenler birbirine eşittir')


kulaniciadi = input('kullanıcı adı:')

if kulaniciadi == 'MBVadam12':
    password = input('şifre:')
    if password == '123456':
        print('login başarılı')
    else:
        print('hatalı parola')
else:
    print(kulaniciadi, 'isimli bir kullanıcı bulunamadı')
