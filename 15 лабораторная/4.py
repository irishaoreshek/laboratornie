print('Введите ненулевые координаты точки')

def Quarter(x, y) :
    if ((x>0) and (y>0)):
        return ('I')
    elif ((x<0) and (y>0)):
        return('II')
    elif ((x<0) and (y<0)):
        return ('III')
    elif ((x>0) and (y<0)):
        return ('IV')

x1=int(input())
y1=int(input())

if ((x1!=0) and (y1!=0)):
    print('ответ =',Quarter(x1,y1),sep=' ')
else:
    print('Введённые координаты не удовлетворяют условию')
    print('Введите ненулевые координаты точки')

x2=int(input())
y2=int(input())

if ((x2!=0) and (y2!=0)):
    print('ответ =',Quarter(x2,y2),sep=' ')
else:
    print('Введённые координаты не удовлетворяют условию')
    print('Введите ненулевые координаты точки')

x3=int(input())
y3=int(input())

if ((x3!=0) and (y3!=0)):
    print('ответ =',Quarter(x3,y3),sep=' ')
else:
    print('Введённые координаты не удовлетворяют условию')
    
    