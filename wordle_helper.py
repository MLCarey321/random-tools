import string
from nltk.corpus import words


def fill_word(word, indices, letters, required, options):
    index = indices[0]
    last_index = len(indices) == 1
    for letter in ([k for k in required.keys() if index not in required[k]] + letters):
        word[index] = letter
        if last_index:
            check_word(word, required, options)
        else:
            length = index+1
            pre = "".join(word[:length])
            if pre in [option[:length] for option in options]:
                fill_word(word, indices[1:], letters, required, options)


def check_word(word, required, options):
    if all(letter in word for letter in required.keys()):
        candidate = "".join(word)
        if candidate in options:
            print(candidate)


with open("input.txt") as reader:
    green = reader.readline().strip().split()
    yellow = reader.readline().strip().split()
    black = list(reader.readline().strip())

template = {i: "" for i in range(5)}
for g in green:
    template[int(g[1])] = g[0]
open_slots = [k for k in template.keys() if template[k] == ""]
unassigned = {y[0]: [int(i) for i in list(y[1:])] for y in yellow}
eligible = [a for a in list(set(string.ascii_lowercase) - set(black) - set(unassigned.keys()))]
dictionary = [word for word in words.words() if len(word) == 5]

fill_word([v for v in template.values()], open_slots, eligible, unassigned, dictionary)
