print('Введите числа A и N')

a = int(input())
n = int(input())

if (n>0):
    x = 1
    st=1

for i in range(1,n+1):
    st=st*a
    x = x+st
    print('ответ =',x ,sep = ' ')
else:
    print('Введите число N, удовлетворяющее услвовию')