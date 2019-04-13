# ex 9.1
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

# ex 9.2


def has_no_e(word):
    index = 0
    while index < len(word):
        if word[index] == 'e':
            return False
        index = index + 1
    return True


checked = has_no_e('fayokemi')
print(checked)


have_no_e = []
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if has_no_e(word):
        print(word)
        have_no_e.append(word)
perc_have_no_e = (len(have_no_e) / 113809) * 100


# ex9.3


def avoids(word, *params):
    for param in params:
        if param in word:
            return False
        return True


def forbidden():
    have_no_forbidden = list()
    fin = open('words.txt')
    new_params = input('forbidden strings are = ')
    for line in fin:
        word = line.strip()
        if avoids(word, *new_params):
            have_no_forbidden.append(word)
            print(len(have_no_forbidden))

forbidden()


# ex9.4


def uses_only(word, *params):
    only_letters = list(*params)
    for w in word:
        if w not in only_letters:
            return False
    return True


check = uses_only('aeiod', 'a','e','i','o','u')
print(check)


# ex9.5

def uses_all(word, *params):
    all_letters = list(*params)
    for letter in all_letters:
        if letter not in word:
            return False
    return True


# ex9.6

'using a for loop'


def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


checking = is_abecedarian('ade')
print(checking)


# ex 9.7


def cartalk1(word):
    n = 0
    previous = word[0]
    for w in word[1:]:
        if w == previous:
            while True:
                cartalk1(word[1:])
        elif w != previous:
            cartalk1(word[1:])
        n = n + 1
        return 'This word does not have three consecutive double letters'
