# Yaay! Our fist exercise here ex7.1
def print_n(s,n):
    while n > 0:
        print(s)
        n = n-1


print_n('I rock my world', 3)

# ex 7.2
import sys


def square_root(a):
    x = 3
    while True:
        y = (x + a / x) / 2
        if abs(y-x) < sys.float_info.epsilon:
            break
        x = y
    return y


result = square_root(4)
print(result)

# '''ex 7.3'''
import math


def test_square_root():
    a = 1
    while a > 0 and a < 10:
        y = square_root(a)
        x = math.sqrt(a)
        print(str(a) + ' ' + str(y) + ' ' + str(x) + ' ' + str(abs(y-x)))
        a = a+1


test_square_root()


# ex7.4

def eval_loop():
    while True:
        user_input = input('> \n')
        if user_input == 'done':
            break
        result = eval(user_input)
        print(result)
    return result


answer = eval_loop()
print(answer)

# ex7.5
import math


def estimate_pi():
    x = 0
    k = 1
    while True:
        print('k =', k)
        a = math.factorial(4*k)
        b = 1103+(26390*k)
        c = (math.factorial(k))**4
        d = 396**(4*k)
        y = (a * b)/(c*d)
        print('y = ', y)
        x = x+y
        print('x =', x)
        if y < 1e-15:
            break
        k = k + 1
    f = (2*math.sqrt(2))/9801
    mi = 1/(f * x)
    return mi














