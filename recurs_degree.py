res = 1

def summa(a, b):
    global res
    if (b == 0):
        return res
    res *= a 
    return summa(a, b-1)

a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))
summa(a, b)
print(f"Число {a} в степени {b} равно {res}")
