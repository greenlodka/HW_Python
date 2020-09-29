a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите число 3: "))

if a * b == c:
    print(a, "умножить на", b, "равно", c)
elif a * b != c:
    print(a, "умножить на", b, "не равно", c)
if a / b == c:
    print(a, "разделить на", b, "равно", c)
elif a / b != c:
    print(a, "разделить на", b, "не равно", c)
if a ** b == c:
    print (a, "в степени", b, "равно", c)
elif a ** b != c:
    print (a, "в степени", b, "не равно", c)
