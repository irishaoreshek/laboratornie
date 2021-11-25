a=int(input())
b=int(input())
c=int(input())

if a<b+c and b<a+c and c<a+b:
    print('Треугольник со сторонами a, b, c существует')
else:
    print('Треугольник со сторонами a, b, c не существует')
