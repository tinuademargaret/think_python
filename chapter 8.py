# ex8.1


def display_backwards(word):
    index = len(word) - 1
    while index >= 0:
        letter = word[index]
        print(letter)
        index = index - 1


display_backwards('Tinuade')

# ex 8.4


def abecedarian_series():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    nuffix = 'uack'
    for letter in prefixes:
        if letter == 'O':
            print(letter + nuffix)
        elif letter == 'Q':
            print(letter + nuffix)

        else:
            print(letter + suffix)


abecedarian_series()


# ex 8.4


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


find('banana', 'a')

# ex8.5


def count(word, a ):
    count = 0
    for letter in word:
        if letter == a:
            count = count + 1
    print(count)


# ex8.6


def counter(word, letter, index):
    count = find(word, letter, index)

    print(count)


counter('banana', 'a', 0)

# ex8.9


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True


rev = is_reverse('pots', 'stop')
print(rev)


# ex8.10


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


palindrome = is_palindrome('noon')
print(palindrome)




