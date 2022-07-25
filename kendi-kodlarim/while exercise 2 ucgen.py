hml = int(input('How many lines do you want to draw: '))
y = int(input('aralarındaki bosluk: '))

x = 1
while x <= hml:
        ilkspace = hml - x
        ikincispace = (hml - x) * 2 + y

        print(ilkspace * ' ' + x * "* " + ikincispace * ' ' + x * '* ')
        x = x + 1

