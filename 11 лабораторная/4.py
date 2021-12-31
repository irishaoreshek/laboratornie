x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("Точка находится в I четверти")

if x < 0 and y > 0:
    print("Точка находится в II четверти")

if x < 0 and y < 0:
    print("Точка находится в III четверти")

if x > 0 and y < 0:
    print("Точка находится в IV четверти")