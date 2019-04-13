# ex3.3
def right_justify(s):
    print(' '*(70-len(s))+s)


right_justify('allen')


# ex3.4 no 2

def do_twice(c, b):
    c(b)
    c(b)

# ex3.4 no 3


def print_twice(b):
    print(b)
    print(b)


do_twice(print_twice, 'spam')


# ex3.4 no 4

def do_four(c, b):
    do_twice(c, b)
    do_twice(c, b)


do_four(print_twice, 'tinu')

# ex3.5 no 1

line = ('+ '+'- '*4)*2 + '+'


def draw_grid():
    print(line)
    do_four(print_twice, '|         |         |')
    print(line)
    do_four(print_twice, '|         |         |')
    print(line)


draw_grid()


# ex3.5 no 1
'''
For four rows line becomes line =('+ '+'- '*4)*3 + '+' and  the function *do_four(print_twice, '|         |         |')
    print(line)* is called two more times
'''
