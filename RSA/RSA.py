p = 2624215969
q = 753915457697
n = p*q
f = (p-1)*(q-1)
print("n = " + str(n) + " f = " + str(f))
e = int(input("Введите 'е': "))
print ("Решите в WolframAlpha уравнение - (d*%d)mod%d=1" % (e, f))
print("для получения d по формуле: %d*n+x" % (f))
x = int(input("Введите х: "))
k = int(input("Введите n: "))
print("d = " + str(f*k + x))

