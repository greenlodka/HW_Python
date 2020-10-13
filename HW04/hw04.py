while True:
    s = input("Введите слово: ")
    if not s:
        break
    s1 = s.lower()
    s2 = s1.strip("'!«‎»‎()-[]{};:'\\,= <>./?@#$%^&*_~'")
    for i, letter in enumerate(s2):
        if i < (len(s2) // 2):
            print(letter)
  
