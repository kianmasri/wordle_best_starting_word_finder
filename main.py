import json
import re


def compare_words(guess: str, key: str):
    contains = list()
    known = list()
    miss = list()
    for i, guess_letter in enumerate(guess):
        flag = True
        if guess_letter == key[i]:
            known.append([i, guess_letter])
            continue
        for key_letter in key:
            if guess_letter == key_letter:
                contains.append([i, guess_letter])
                flag = False
        if flag:
            miss.append(guess_letter)
    return [contains, known, miss]


def filter_words(wordlist: list, guess: str, key: str):
    [contains, known, miss] = compare_words(guess, key)
    new_words = wordlist
    for occurrence in known:
        r = re.compile(r"^.{" + str(occurrence[0]) + r"}" + occurrence[1])
        new_words = list(filter(r.match, new_words))
    for occurrence in contains:
        r = re.compile(r".*" + str(occurrence[1]) + r"+")
        new_words = list(filter(r.match, new_words))
        r = re.compile(r"^.{" + str(occurrence[0]) + r"}(?!" + occurrence[1] + r")")
        new_words = list(filter(r.match, new_words))
    for occurrence in miss:
        r = re.compile(r"^((?!" + occurrence + ").)*$")
        new_words = list(filter(r.match, new_words))
    return new_words


words = list(json.load(open('wordle_dictionary.json')))
answers = list(json.load(open('wordle_answer_dictionary.json')))
performance = dict()
f = open("output.txt", "a")
for guess in words:
    performance[guess] = 0
    for key in answers:
        new_words = filter_words(answers, guess, key)
        performance[guess] += len(new_words)
    out = guess + "\t" + str(performance[guess] / 12972) + "\n"
    f.write(out)
    print(out)
print(min(performance, key=performance.get))
