print('Введите значение N>1')

n=int(input())

if (n>1):
    x=0
    k=0
while (x<n):
    k+=1
    x+=k
    print('значение k =',k,'сумма =',x, sep=' ')

else:
    print('Введите значение, удовлетворяющее условию')