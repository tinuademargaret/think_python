# ex12.1


def sum_all(*args):
    a = 0
    for arg in args:
        a += arg
    return a


print(sum_all(1, 2, 3, 4, 5))


# ex12.2
import random


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    t.sort(reverse=True)
    res = []
    for length, _, word in t:
        res.append(word)
    return res


# ex12.3


def most_frequent(word):
    f = []
    for w in word:
        f.append((word.count(w), w))
    f.sort(reverse=True)
    res = []
    for frequency, letter in f:
        res.append(letter)
    return res


# ex12.4


# def anagrams(filename):
#     data = open(filename).read()
#     a = ('a', 'd', 'e', 'l', 's', 't')
#     b = ('a', 'e', 'e', 'i', 'n', 'r', 'r', 's', 't')
#     c = ('a', 'e', 'e', 'g', 'g', 'i', 'n', 'n', 'r', 't')
#     d = ('e', 'e', 'l', 'm', 'r', 's', 's', 't')
#     e, f, g, h = [], [], [], []
#     for word in data:


