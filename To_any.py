li = input("Введите числа в 10-ичной системе через пробел\n").split()
new_list = []
for i in li:
    new_list.append(hex(int(i)))  # запишите hex oct или bin
for i in new_list:
    print(i[2:], end=" ")
