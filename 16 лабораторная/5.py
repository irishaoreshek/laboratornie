print('Введите N')
n = int(input())

a=[i+1 for i in range(n)]
chet=[]
nechet=[]

for i in range(len(a)):
    if (i%2 == 0):
        chet.append(a[i])
    else:
        nechet.append(a[i])
        nechet.reverse()

print('изначальный массив =', a, sep=' ')
print('массив с нечётными номерами =', chet, sep=' ')
print('массив с чётными номерами =', nechet, sep=' ')