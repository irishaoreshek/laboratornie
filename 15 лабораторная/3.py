print('Введите значения R1 и R2, R1>R2')

def RingS(r1,r2):
    return 3.14*(r1**2-r2**2)
    
r1=int(input())
r2=int(input())

if (r1>r2):
    print('ответ =',RingS(r1,r2),sep=' ')
else:
    print('Введите значения, удовлетворяюще условию')
    print('Введите значения R1 и R2, R1>R2')
    
r3=int(input())
r4=int(input())

if (r3>r4):
    print('ответ =',RingS(r3,r4),sep=' ')
else:
    print('Введите значения, удовлетворяюще условию')
    print('Введите значения R1 и R2, R1>R2')
    
r5=int(input())
r6=int(input())

if (r5>r6):
    print('ответ =',RingS(r5,r6),sep=' ')
else:
    print('Введите значения, удовлетворяюще условию')
    