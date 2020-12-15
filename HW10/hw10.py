import random

def ok(filename):
    with open(filename, encoding= "utf-8") as f:
        words = f.read().split()
    return random.choice(words)

noun = ok("nouns.txt")
conjverb = ok("conjverbs.txt")
verb = ok("verbs.txt")
place = ok("places.txt")
motiverb = ok("motiverb.txt")


def organizer():
    sentence1 = noun.title() + " " + conjverb + " " + verb + " " + "в" + " " + place + '.'
    sentence2 = conjverb.title() + " ли " + noun + " " + verb + " " + "в" + " " + place + '?'
    sentence3 = noun.title() + " не " + conjverb + " " + verb + " " + "в" + " " + place + '.'
    sentence4 = "Если " + noun + " " + conjverb + " " + verb + " " + "в" + " " + place + ", то пусть " + conjverb + "."
    sentence5 = motiverb.title() + " в " + place + "!"
    my_array = [sentence1 + "\n",sentence2 + "\n",sentence3 + "\n",sentence4 + "\n", sentence5 + "\n"]
    random.shuffle(my_array)
    return "".join(my_array)


def main():
    print(organizer())
if __name__ == "__main__":
    main()

