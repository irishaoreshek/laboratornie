A = int(input("A="))
B = int(input("B="))

if A == B:
    A=0
    B=0
    
if A>B:
    Bcopy = A 
    print("A=", A)
    print("B=", Bcopy)
else:
    Acopy = B 
    print("A=", Acopy)
    print("B=", B)