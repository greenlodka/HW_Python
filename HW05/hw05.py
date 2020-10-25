word = input("Введите слово: ")
word = word.lower()
l = len(word)
code = word
a = 0
print(word)
for a in range(l - 1):
    for i,letter in enumerate(word):
        if i == l - 1:
             code += code[0]
        elif i < l:
            code += code[i + 1]
        else:
            break
    code = code[-l : ]
    a += 1
    print(code)
