
print(" begin of file  -------------------------------------")

print("\n test 1 -------------------------------------")
print('hello')

print('{}'.format('hello'))
print('{}'.format(1211))

print('hello {} world'.format('phyton'))
strval = 'phyton'
print('hello {} {}'.format(strval   , 'world'))
strval1 = 'hello'
strval2 = 'phyton'
strval3 = 'world'
print('{0} {1} {2}'.format(strval1, strval2, strval3))
print('{0} {2} {1}'.format(strval1, strval2, strval3))
print('{0} {0} {1} {2}'.format(strval1, strval2, strval3))
print('{:.15}'.format('hello phyton world'))
print('{:.5}'.format('hello phyton world'))
print('{:*>60}'.format('phyton world'))

print("n end of file -------------------------------------")

print('{:d}'.format(12))
print('{:d}'.format(-12))
print('{:+d}'.format(12))

ival = 123456
print('{:d}'.format(ival))
print('{:20d}'.format(ival))
print('{:020d}'.format(ival))
print('{:,d}'.format(ival))
print('{:d}'.format(ival))

fval = 123.456789
print('{:f}'.format(fval))
print('{:.2f}'.format(fval))
print('{:10.4f}'.format(fval))
print('{:010.4f}'.format(fval))