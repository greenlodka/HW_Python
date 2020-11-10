lines = []
while True:
    line = input("Введите слово: ")
    line = line.lower()
    lines.append(line)
    if line  == " ":
        break
for line in lines:
    if line != lines[2]:
        line1 = line[::-1]
        new_line = []
        for i, sym in enumerate(line1):
            if i % 2 == 0:
                new_line.append(sym)
            else:
                continue
        print("".join(new_line))
