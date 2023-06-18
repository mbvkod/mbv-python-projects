listnum = [a for a in range(1, 6)]
print(listnum)

print('\n')

listnum = [b**2 for b in range(1, 6)]
print(listnum)

print('\n')


div2list = [c for c in range(1, 51) if c % 2 == 0]
print(div2list)

print('\n')

div6list = [d for d in range(1, 51) if d % 6 == 0]
print(div6list)

print('\n')

for e in range(1, 51):
    if e % 5 == 0:
        print(e)

print('\n')

meyvelist = ['elma', 'armut', 'karpuz']
meyvelistupper = [x.upper() for x in meyvelist]
meyvelistshort = [y[0:2] for y in meyvelist]
meyvelistV2 = [z for z in meyvelist if 'e' in z]

print(meyvelist)
print(meyvelistupper)
print(meyvelistshort)
print(meyvelistV2)
