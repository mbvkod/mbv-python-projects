# list           sıralanabilen     değiştirilebilir      indexli     yinelenebilir    ['armut', 'çilek']
# tuple          sıralanabilen    değiştirlemez          indexli     yinelenebilir    ('armut', 'çilek')
# set            sırasız          değiştirilebilir       indexsiz    yinelenemez      {'armut', 'çilek'}
# dictionary     sırasız          değiştirilebilir       indexli     yinelenemez      {'burak':12, 'ahmet': 'mühendis'}

personel1 = {
    'isim': 'burak',
    'yaş': 15,
    'meslek': 'öğrenci'
}
# print(personel1)

# isimval = personel1['isim']
# print(isimval)

# yasval = personel1['yaş']
# print(yasval)

# personel1['meslek'] = 'futbolcu'
# print(personel1['meslek'])

# print(personel1)
# personel1['cinsiyet'] = 'erkek'


# print(help(dict))
# print(help(dict.get))


# get
# print(personel1)
# isimval = personel1['isim']
# isimval = personel1.get('isim')
# print(isimval)


# len/ uzunluk
# print(len(personel1))


# pop/ istediğin değişkeni siler
# print(personel1)
# silinenval = personel1.pop('yaş')
# print(personel1)
# print(silinenval)


# popitem/ son eklenen değişkeni siler
# print(personel1)
# silinenval = personel1.popitem()
# print(personel1)
# print(silinenval)


# del/ komple yok eder
# print(personel1)
# del personel1


# clear/ içindeki valueları siler
# print(personel1)
# personel1.clear()
# print(personel1)


# dict
# personel2 = dict(
#     isim='burak',
#     yaş=28,
#     meslek='öğrenci'
# )
# print(personel1)
# print(personel2)
