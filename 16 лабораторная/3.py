print('Введите N, N>2')
n = int(input())
print('Введите A')
a = int(input())
print('Введите B')
b = int(input())

m=[a,b]

if (n>2):
    for i in range(2,n):
        k = sum(m)
        m.append(k)
        print('ответ =',m, sep = ' ')
else:
    print('Ввеите значение, удовлетворяющее условию')