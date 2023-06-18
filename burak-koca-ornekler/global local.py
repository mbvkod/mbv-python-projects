num1 = 10  # global


def func1():
    num2 = 20  # local
    print(num1)
    print(num2)


func1()
print(num1)

print('------------------------------------------------------------------------------------------------')

num = 10
print(num)


def func2():
    num = 20
    print(num)


func2()
print(num)

print('------------------------------------------------------------------------------------------------')

sayi = 10
print(sayi)


def func3():
    global sayi
    sayi = 20
    print(sayi)


func3()
print(sayi)
