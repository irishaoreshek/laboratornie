print('Введите числа A и N')

a = int(input())
n = int(input())

if (n>0):
    x = 1
    y=1

for i in range(1,n+1):
    y=(-1)*y*a
    x = x+y
    print('ответ =',x ,sep = ' ')
else:
    print('Введите число N, удовлетворяющее услвовию')