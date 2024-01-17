sum1 = 0

def summa(a, b):
    global sum1
    if (b == 0):
        return sum1
    sum1 += a 
    return summa(a, b-1)

a = int(input("Введите 1 множитель: "))
b = int(input("Введите 2 множитель: "))
summa(a, b)
print(f"Произведение {a} на {b} равно {sum1}")
