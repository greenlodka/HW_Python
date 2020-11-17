f = open("bloknapole.txt", encoding="UtF-8")
words = []
for line in f.readlines():
    line = line.split(" ")
    if line != ["\n"]: #учитываем пустые строки в стихе
        words.append(len(line))

words_num = len(words)
words_sum = 0
for char in words:
    words_sum += char
average = words_sum // words_num
print("Среднее число слов в строке: ", average)

max = 1
for num in words:
    if num > max:
        max = num
min = 1 #в строке должно быть минимум одно слово
result = max // min
print("Самая короткая строка в ", result, "раз короче самой длинной")

five_plus = 0
for char in words:
    if char > 5:
        five_plus += 1
five_plus_per = five_plus * 100 // words_num
print(five_plus_per, "% строк содержит больше 5 слов")

f.close()
