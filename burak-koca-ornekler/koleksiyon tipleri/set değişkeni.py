# list           sıralanabilen     değiştirilebilir      indexli     yinelenebilir    ['armut', 'çilek']
# tuple          sıralanabilen    değiştirlemez          indexli     yinelenebilir    ('armut', 'çilek')
# set            sırasız          değiştirilebilir       indexsiz    yinelenemez      {'armut', 'çilek'}
# dictionary     sırasız          değiştirilebilir       indexli     yinelenemez      {'burak':12, 'ahmet': 'mühendis'}


meyveset = {'elma', 'armut', 'kivi', 'muz', }
# print(meyveset)
# print(type(meyveset))

# print(help(set))

# add
# print(meyveset)
# meyveset.add('karpuz')
# print(meyveset)

# update
# print(meyveset)
# meyveset.update(['burak', 'sad'])
# print(meyveset)

# len
# print(meyveset)
# print(len(meyveset))

# remove/ olmayan değişken verirsek hata verir
# print(meyveset)
# meyveset.remove('armut')
# print(meyveset)

# discard/ olmayan değişken verirsek hata vermez
# print(meyveset)
# meyveset.discard('1eafds')
# print(meyveset)

# pop/ index olmadığı için rastgele eleman siler
# print(meyveset)
# silinenmeyve = meyveset.pop()
# print(meyveset)
# print(silinenmeyve)

# clear/ bütün seti siler
# print(meyveset)
# meyveset.clear()
# print(meyveset)

# del/ seti ortadan kaldırır
# print(meyveset)
# del meyveset
# print(meyveset)