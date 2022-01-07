print('Введите значение N>1')

n=int(input())

if (n>1):
    f1=1
    f2=1
    f=0
    k=2
while(f<n):
    k+=1
    f=f1+f2
    f2=f1
    f1=f
    print('ответ =', k, sep=' ')
else:
    print('Введите значение, удовлетворяющее условию')