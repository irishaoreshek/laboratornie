n = int(input())
m = int(input())
if n in range (1,31+1):
    if (n==1):
        n1 = 'первое'
    elif (n==2):
        n1 = 'второе'
    elif (n==3):
        n1 = 'третье'
    elif (n==4):
        n1 = 'четвертое'
    elif (n==5):
        n1 = 'пятое'
    elif (n==6):
        n1 = 'шестое'
    elif (n==7):
        n1 = 'седьмое'
    elif (n==8):
        n1 = 'восьмое'
    elif (n==9):
        n1 = 'девятое'
    elif (n==10):
        n1 = 'десятое'
    elif (n==11):
        n1 = 'одиннадцатое'
    elif (n==12):
        n1 = 'двенадцатое'
    elif (n==13):
        n1 = 'тринадцатое'
    elif (n==14):
        n1 = 'четырнадцатое'
    elif (n==15):
        n1 = 'пятнадцатое'
    elif (n==16):
        n1 = 'шестнадцатое'
    elif (n==17):
        n1 = 'семнадцатое'
    elif (n==18):
        n1 = 'восемнадцатое'
    elif (n==19):
        n1 = 'девятнадцатое'
    elif (n==20):
        n1 = 'двадцатое'
    elif (n==21):
        n1 = 'двадцать первое'
    elif (n==22):
        n1 = 'двадцать второе'
    elif (n==23):
        n1 = 'двадцать третье'
    elif (n==24):
        n1 = 'двадцать четвертое'
    elif (n==25):
        n1 = 'двадцать пятое'
    elif (n==26):
        n1 = 'двадцать шестое'
    elif (n==27):
        n1 = 'двадцать седьмое'
    elif (n==28):
        n1 = 'двадцать восьмое'
    elif (n==29):
        n1 = 'двадцать девятое'
    elif (n==30):
        n1 = 'тридцатое'
    elif (n==31):
        n1 = 'тридцать первое'
else:
    print('Введите значение, удовлетворяющее дипозону')
if m in range (1,12+1):
    if (m==1):
        m1 = 'января'
    elif (m==2):
        m1 = 'февраля'
    elif (m==3):
        m1 = 'марта'
    elif (m==4):
        m1 = 'апреля'
    elif (m==5):
        m1 = 'мая'
    elif (m==6):
        m1 = 'июня'
    elif (m==7):
        m1 = 'июля'
    elif (m==8):
        m1 = 'августа'
    elif (m==9):
        m1 = 'сентября'
    elif (m==10):
        m1 = 'октября'
    elif (m==11):
        m1 = 'ноября'
    elif (m==12):
        m1 = 'декабря'
else:
    print('Введите значение, удовлетворяющее дипозону')
print (n1,m1,sep=' ')
