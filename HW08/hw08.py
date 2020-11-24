fw = open("doctor100.txt","w", encoding = "utf-8")
f = open("doctor.txt", encoding = "utf-8")
list = []

for line in f:
    line = line.lower()
    for word in line.split():
        word = word.strip("'!«»()-[]{};:'\\,= <>./?@#$%^&*_~'")
        list.append(word)

for i in list:
     if list.count(i) == 1:
        i += "\t1"
     elif list.count(i) > 1:
        i += "\t+"
     fw.write(i + "\n")

f.close()
fw.close()