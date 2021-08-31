uzunluk = float(input('uzunlugun ne: '))
cesit = input('santimetre/metre: ')

if cesit == 'metre'.lower():
    santimetre  = uzunluk * 100
    print('santimetre uzunlugun: ' + str(santimetre))



else:
    metre = uzunluk / 100
    print('metre cinsinden uzunlugun' + str(metre))
