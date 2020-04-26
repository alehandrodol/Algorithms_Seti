e = 422113
n = 1270807
d = 606193
li = input("Введите числа для кодировки/декодировки: ").split()
cod = int(input("Введите 1 - если открытый ключ, и 0 - если закрытый ключ: "))

if cod:
    for i in li:
        i = int(i)
        res = (i ** e) % n
        print(res, end=" ")
else:
    for j in range(1000):
        for i in li:
            i = int(i)
            res = (i ** d) % n
            print(res, end=" ")
            li[0] = res
        if res == 7171:
            print(j)
            break
