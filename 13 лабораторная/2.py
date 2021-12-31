print('Введите число N')

n = int(input())

if (n>0):
    x = 1
for i in range(1,n+1):
    x = x*(1+0.1*i)
    print('ответ =',x ,sep = ' ')
else:
    print('Введите число N, удовлетворяющее услвовию')