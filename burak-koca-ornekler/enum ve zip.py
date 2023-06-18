meyvelist = ['elma', 'armut', 'kavun', 'karpuz']
for meyve in enumerate(meyvelist):
    print(type(meyve))
    print(meyve)

print('\n')

for sira, meyve in enumerate(meyvelist):
    print('{}. indexi:  {}'.format(sira, meyve))

print('\n')

meyvelist = ['elma', 'armut', 'kavun', 'karpuz']
fiyatlist = [12.75, 10, 23]
for a in zip(meyvelist, fiyatlist):
    print(a)
    print(type(a))

print('\n')

kisilist = ['burak', 'veysel', 'ömür']
puanlist = [100, 99, 70]
okullist = ['bk', 'bağkoleji', 'karabaş']

for kisi, puan, okul in zip(kisilist, puanlist, okullist):
    print('{} {} puan aldı, {} okuluna gidiyor'.format(kisi, puan, okul))
