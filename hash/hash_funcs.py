import requests
string = "e0d73214"
text = ""
a = 65
b = 65
c = 65
d = 65
s = chr(a) + chr(b) + chr(c) + chr(d)
url = 'https://md5calc.com/hash?algo=crc32b&str=' + s + '&output=plain'
r = requests.get(url)
text = r.text
print(text)
if string == text:
    print("Ура ответ: " + s)
