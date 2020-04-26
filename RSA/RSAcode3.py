e = 421121
n = 813077
my = 123
print("Решите в WolframAlpha уравнение (%d ^ %d)mod%d" % (my, e, n))
z = int(input("Напишите результат: "))
print("Решите в WolframAlpha уравнение p * q = %d" %(n))
p = int(input("Напишите первый корень не равный 1 и числу n: "))
q = int(input("Напишите второй корень: "))
f = (p-1) * (q-1)
print ("Решите в WolframAlpha уравнение - (d*%d)mod%d=1" % (e, f))
print("число х в данной формуле и будет являться числом d: %d*n+x" % (f))
d = int(input("Введите х: "))
res = (z**d) % n
if (res == my):
    print("It works")
    print(d)
