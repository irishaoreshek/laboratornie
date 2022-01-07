n = int(input())
z = 'зелён'
k = 'красн'
zh = 'жёлт'
b = 'бел'
ch = 'чёрн'
jiv_1 = 'крысы'
jiv_2 = 'коровы'
jiv_3 = 'тигра'
jiv_4 = 'зайца'
jiv_5 = 'дракона'
jiv_6 = 'змеи'
jiv_7 = 'лошади'
jiv_8 = 'овцы'
jiv_9 = 'обезьяны'
jiv_10 = 'курицы'
jiv_11 = 'собаки'
jiv_12 = 'свиньи'
def f(n):
    if (((n%10) == 0) or ((n%10) == 1)):
        color = b 
    elif (((n%10) == 2) or ((n%10) == 3)):
        color = ch 
    elif (((n%10) == 4) or ((n%10) == 5)):
        color = z
    elif (((n%10) == 6) or ((n%10) == 7)):
        color = k 
    elif (((n%10) == 8) or ((n%10) == 9)):
        color = zh
    else:
        color = 0
    if (((n%12) == 0) or ((n%12) == 1) or ((n%12) == 2) or ((n%12) == 3) or ((n%12) == 4) or ((n%12) == 5) or ((n%12) == 9) or ((n%12) == 10) or ((n%12) == 11)):
        rod = 'ой'
    elif (((n%12) == 6) or ((n%12) == 7) or ((n%12) == 8)):
        rod = 'ого'
    else:
        rod = 0
    if ((n+8)%12 == 0):
        jiv = jiv_1
    elif ((n+8)%12 == 1):
        jiv = jiv_2
    elif ((n+8)%12 == 2):
        jiv = jiv_3
    elif ((n+8)%12 == 3):
        jiv = jiv_4
    elif ((n+8)%12 == 4):
        jiv = jiv_5
    elif ((n+8)%12 == 5):
        jiv = jiv_6
    elif ((n+8)%12 == 6):
        jiv = jiv_7
    elif ((n+8)%12 == 7):
        jiv = jiv_8
    elif ((n+8)%12 == 8):
        jiv = jiv_9
    elif ((n+8)%12 == 9):
        jiv = jiv_10
    elif ((n+8)%12 == 10):
        jiv = jiv_11
    elif ((n+8)%12 == 11):
        jiv = jiv_12
    else:
        jiv = 0
    return ('Год', color, rod, jiv)
print (f(n))
