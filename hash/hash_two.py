import binascii

string = "0x794171b0"
text = ""
a = 97
b = 99
c = 104
d = 105
e = 97
f = 97
g = 97
h = 97
flag = False

while a <= 122:  # 65 90 97 122
    while b <= 122:
        while c <= 122:
            while d <= 122:
                while e <= 122:
                    while f <= 122:
                        while g <= 122:
                            while h <= 122:
                                s = bytes([a, b, c, d, e, f, g, h])
                                text = hex(binascii.crc32(s))
                                print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e) + " " + str(f) + " " + str(g) + " " + str(h))
                                print(text)
                                if string == text:
                                    flag = True
                                    print("Ура ответ: " + chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f) + chr(g) + chr(h))
                                    break
                                h += 1
                            h = 97
                            g += 1
                            if flag:
                                break
                        f += 1
                        g = 97
                        if flag:
                            break
                    e += 1
                    f = 97
                    if flag:
                        break
                e = 97
                d += 1
                if flag:
                    break
            d = 97
            c += 1
            if flag:
                break
        c = 97
        b += 1
        if flag:
            break
    b = 97
    a += 1
    if flag:
        break
