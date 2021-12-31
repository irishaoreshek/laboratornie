A = int(input("Число A:"))
B = int(input("Число B:"))
C = int(input("Число C:"))

AB = abs(A-B)
AC = abs(A-C)

print("Расстояние от A до B:",AB)
print("Расстояние от A до C:",AC)

if AB < AC:
    print("В ближе к A")
elif AB > AC:
    print("C ближе к A")
else:
    print("B и C равноудалены от A")