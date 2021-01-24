import re

#Часть1

smileregex = r'(?P<head>;|:|8|&|=){1,2}(?P<body>(-|−|–|—])*)(?P<tail>(\(|\))+)'

mysmile = input("Введите смайлик: ")
x = re.search(smileregex, mysmile)
if x:
    print(x.group('tail', 'body', 'head'))
else:
    print("Это не похоже на смайлик, попробуте еще раз")

#Часть2

useful_strings = []
regex = r'(?<![$€¥])\d{3,4}(?!\s[год|г\.|гг\.])'

my_file = open('filere.txt','r',encoding = 'UTF-8')
file_strings = my_file.readlines()
print(file_strings)

for string in file_strings:
    result = re.search(regex,string)
    if result:
        useful_strings.append(result.group())
print(set(useful_strings))




