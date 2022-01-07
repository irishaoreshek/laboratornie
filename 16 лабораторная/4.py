print('Введите N')
n = int(input())

k=n//2
a=[i+1 for i in range(n)]
m=[]

for i in range(0,k):
    m.append(a[i])
    m.append(a[n-i-1])
    if (2*k < n):
        m.append(a[k])
        print('ответ =', m, sep=' ')