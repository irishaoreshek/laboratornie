print('Введите N, N>1')
n = int(input())
print('Введите A')
a = int(input())
print('Введите D')
d = int(input())

m=[a]*n
if (n>1):
    for i in range(1,len(m)):
        m[i]=a*d
        a = a*d
        print('ответ =',m, sep = ' ')
else:
    print('Ввеите значение, удовлетворяющее условию')