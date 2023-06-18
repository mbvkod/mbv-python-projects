def a(num):
    return num * 2


print(a(4))


print('------------------------------------------------------------------------------------------------------------')


b = lambda num: num * 2
print(b(14))


print('------------------------------------------------------------------------------------------------------------')


c = lambda num1, num2: num1 + num2
print(c(12, 3))


print('------------------------------------------------------------------------------------------------------------')


d = lambda *numbers: sum(numbers)
print(d(2, 3, 1, 2,))


print('------------------------------------------------------------------------------------------------------------')


def func(num1):
    return lambda num2: num2 * num1


funcdoubler = func(2)  # num2: num2 * 2
functripler = func(3)  # num2: num2 * 3

print(funcdoubler(10))
print(functripler(10))


print('----------------------------------------------------------------------------------------------------------')


mainfunc = lambda num1, num2: num1 + num2(num1)
# mainfunc = lambda 2, num2: 2 + num2(2)

print(mainfunc(2, lambda x: x*2))
print(mainfunc(3, lambda x: x * 2))

print('---------------------------------------------------------------------------------------------------------')


total = lambda *numbers: sum(numbers)
print(total(1, 2, 3, 4, 5, 6, 7, 8, 9))
