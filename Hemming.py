fifteen = input("Введите 15 битные числа через пробел\n").split()

first = 0
second = 0
third = 0
fourth = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

new_list = []

for i in fifteen:
    first = 0
    second = 0
    third = 0
    fourth = 0
    ind = 1
    for j in i:
        n = int(j)
        if n == 1:
            if ind % 2 == 1:
                first += 1

            ost4 = ind % 4
            if ost4 == 2 or ost4 == 3:
                second += 1

            if ind in nums[3:7] or ind in nums[11:15]:
                third += 1
            if ind >= 8:
                fourth += 1
        ind += 1
    first %= 2
    second = (second % 2) * 2
    third = (third % 2) * 4
    fourth = (fourth % 2) * 8
    num = first + second + third + fourth
    if num != 0:
        new_num = 1 - int(i[num-1])
        new_str = str(new_num)
        i = i[:num-1] + new_str + i[num:]
    res = i[2] + i[4:7] + i[8:]
    new_list.append(res)
string = ""
res_list = []
for i in new_list:
    string += i
while len(string) > 0:
    res_list.append(int(string[:8], 2))
    string = string[8:]
for i in res_list:
    print(i, end=" ")
