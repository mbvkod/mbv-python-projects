hml = int(input('How many lines do you want to draw: '))
x = 1


while x <= hml -1 :
        space = hml - x
        print(space * ' ' + x * "* ")
        x = x + 1



x = hml
while x >= 0:
        space = hml - x
        print(space * ' ' + x * '* ')
        x = x - 1