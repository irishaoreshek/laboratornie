print('Введите значения A и B, A>B')

a = int(input())
b = int(input())

if (a>b):
    while (a-b>=0):
        a = a-b
        print('ответ =', a, sep = ' ')
else:
    print('Введите значениия, удовлетворяющие условию')