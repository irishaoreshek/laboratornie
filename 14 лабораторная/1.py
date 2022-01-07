print('Введите значения A и B, A<B')

a = int(input())
b = int(input())

if (a<b):
    for i in range(a,b+1):
        for n in range(1,i+1):
            print('ответ =', i, sep=' ')
else:
    print('Введите значениия, удовлетворяющие условию')