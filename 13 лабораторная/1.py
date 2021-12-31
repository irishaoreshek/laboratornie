print('Введите цену 1 кг конфет')

n = int(input())

for i in range (1,10+1):
    a = i*0.1*n
    print(i*0.1,'кг',': ',a, sep = ' ')