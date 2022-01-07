print('Введите число')
def Fact2(n):
    x = 1
    if (n%2 == 0):
        y = 2
        while y <= n:
            x = x * y
            y = y + 2 
        return x
    else:
        y = 3
        while y <= n:
            x = x * y
            y = y + 2
        return x
n=int(input())
print('ответ =',Fact2(n),sep=' ')
