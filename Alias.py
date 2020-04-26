num = (input("введите двоичный код для разжатия, с любыми пробелами \n"))
num = num.replace(" ", "")
while num[-1] == "0":
    num = num[:len(num)-1]
first = num[0]
num = num[1:]
zer_count = 0
ind = 0
arr = []
arr2 = []
arr3 = []
newnum = ""
while len(num) > 0:
    if num[ind] == '0':
        zer_count += 1
    else:
        arr.append(num[zer_count:zer_count + zer_count+1])
        num = num[zer_count + zer_count+1:]
        zer_count = 0
        ind = -1
    ind += 1

for i in arr:
    arr2.append(int(i, 2))

for i in arr2:
    newnum += first * i
    if first == "0":
        first = "1"
    else:
        first = "0"

for i in range(len(newnum), 0, -1):
    if i%4 == 0 and i != 0:
        newnum = newnum[:i] + " " + newnum[i:]
li = []
for i in newnum:
    if i == " ":
        x = 5*len(li)
        li.append(hex(int(newnum[x:x+4], 2)))
counter = 0
res = ""
for i in li:
    if counter % 2 == 0 and counter != 0:
        res += " "
    res += i[2]
    counter += 1

print(res)
