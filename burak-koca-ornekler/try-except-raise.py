print(1)
print(2)

try:
    print(x)
except:
    print('x değişkenşi tanımlanmamış')

print(4)
print(5)

print('-------------------------------------------------------------------------------------------------------')

num1 = 10
try:
    num2 = float(input('bölen sayı giriniz'))
    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print('0 değeri girilemez')
except ValueError:
    print('lütfen sayı giriniz'),
except:
    print('tanımlanamayan hata')
else:
    print('işlem başarılı')
finally:
    print('bu kod bloğu her koşul altında çalışcak')

print('-------------------------------------------------------------------------------------------------------')

# sayi = 0
# if sayi == 0:
#     raise Exception('Değer 0 olamaz')

print('-----------------------------------------------------------------------------------------------------')

# sayi = 0
# if sayi == 0:
#     raise ZeroDivisionError('Değer 0 olaamaz')

print('-----------------------------------------------------------------------------------------------------')

val = 'asd'
if val != int or float:
    raise ValueError('lütfen sayısal ifade girin')














