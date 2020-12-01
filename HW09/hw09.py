with open("amh.tsv", encoding = "utf-8") as f:
    f_line = f.readline()
    f_notline = f.read()
l = []
d = {}
for char in f_line:
    if char != "\t" and char != "\n":
        l.append(char)  #получаем лист с гласными
char = f_notline.split() #все символы файла
for i, sym in enumerate(char):
    if i == 0:
        seq_num = i #записываем первую согласную
    elif (i - seq_num) // 8:
        seq_num = i #записываем согласные
    else:
        d[sym] = char[seq_num] + l[i - 1 - seq_num] #потому что гласные смещены на одну
print(d)

with open("ch_am.txt", encoding = "utf-8") as g:
    g = g.read()
    for char in g:
        if char in d:
            char = d[char]
    print(g)
