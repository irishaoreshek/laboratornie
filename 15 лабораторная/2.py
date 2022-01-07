print('Введите два числа A и B')

def sign(x):
    if (x<0):
        return -1
    if (x==0):
        return 0
    if (x>0):
        return 1

a=int(input())
b=int(input())

print('ответ =', sign(a)+sign(b), sep=' ')