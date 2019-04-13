# ex6.1


def compare(x, y):
    if x > y:
        return '1'
    elif x == y:
        return '0'
    elif x < y:
        return '-1'


# ex6.2
import math


def hypotenuse(a,b):
    h = math.sqrt((a**2)+(b**2))
    return h

# ex6.3


def is_between(x, y, z):
    print('i got here')
    if x <= y and y <= z:
        return True
    else:
        return False


val = is_between(1, 4, 3)
print(val)

# ex6.5


def ack(m, n):
    if m == 0:
        result = n+1
        return result
    elif m > 0 and n == 0:
        result = ack(m-1, 1)
        return result
    elif m > 0 and n > 0:
        recursive = ack(m, n-1)
        result = ack(m-1, recursive)
        return result


answer = ack(3, 4)
print(answer)

# ex6.6 palindrome.py no 1


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


test = middle(' ')
print(test)

# ex6.6 palindrome.py no 2


def is_palindrome(word):
    if len(word) == 1:
        return True
    if first(word) == last(word):
        print(middle(word))
        result = is_palindrome(middle(word))
        return result
    else:
        return False


result = is_palindrome(' ')
print(result)

'''you might want to ask what if the initial word has a length of one? of course! it'll return true and it'll be correct since a one letter word is 
is spelled the same backward and forward. From the few examples we've seen concerning recursion you'll notice that the functions always start with the base case so that the recursive function would 
always have something to return'''

# ex 6.7


def is_power(a, b):
    if (a/b) % b == 0:
        return True
    if a % b == 0:
        result = is_power(a/b, b)
        return result
    else:
        return False


answer = is_power(8, 2)
print(answer)

# ex6.8 : Greatest Common Divisor (GCD)


def gcd(a, b):
    if b == 0:
        return a
    if b > 0:
        r = a % b
        result = gcd(b, r)
        return result


answer = gcd(8, 4)
print(answer)







