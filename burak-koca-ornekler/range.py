rngval = range(10)
print(type(rngval))
print(rngval)
print(*rngval),

print('\n')

ival = 0
while ival < 10:
    print(ival)
    ival += 1

print('\n')

listval = [22, 31, 1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 11, 12]
for a in listval:
    if 10 < a > 0:
        continue
    print(a)

print('\n')

for b in rngval:
    print(b)

print('\n')

for c in range(20, 31):
    print(c)

print('\n')

for d in range(30):
    if 10 <= d <= 20:
        print(d)

for e in range(0, 101, 5):
    print(e)

print('\n')

for f in range(50, 10, -2):
    print(f)

print('\n')

g = 1
while g < 10:
    print('*' * g)
    g += 1

while g > 0:
    print('*' * g)
    g -= 1
print(g)

print('\n')

for h in range(1, 11):
    print('*' * h)

for i in range(9, 0, -1):
    print('*' * i)
