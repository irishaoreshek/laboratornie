A=int(input())
B=int(input())
C=int(input())

S_pr=A*B
S_kv=C**2

print('количество квадратов, расмещенных на прямоугольнике =', S_pr//S_kv)
print('площадь незанятой части прямоугольника =', S_pr%S_kv)
