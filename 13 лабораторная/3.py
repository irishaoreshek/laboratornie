print('Введите число N')

n = int(input())

if (n>0):
    x = 0

for i in range(1,n+1):
    x=x+(2*i-1)
    print('результат =',x,sep = ' ')
else:
    print('Введите число N, удовлетворяющее услвовию')