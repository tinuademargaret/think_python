# ex5.2


def do_n(d, n):
    if n <= 0:
        return
    d()
    do_n(d, n-1)


'''
This function is a recursive function i.e it calls itself the process of it calling itself is recursion.
In the first line it takes a function object d and a number n as an argument and calls  the function object 
n times. For example if we want to call d two times we make n = 2. since n = 2 and not <= 0 the if statement is false 
and the function d is returned. In the last line the function calls itself again but with n = 1. It continues like that
until n= 0, then the if statement is true and the return statement exits the function.
'''

'''let's take the do_four exercise from chapter3 again'''


def do_four(c, n):
    if n <= 0:
        return
    c()
    do_four(c, n-1)


'''In this case we'll set n to be 4 since we want the function to be called four times. This doesn't solve the problem 
since we want only two lines of code in the function. Any Idea on how we can improve on this? Share your solution @
www.perimeter.org'''


# ex5.3 no 1


def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, fermat was wrong!')
    else:
        print("No, that doesn't work")


# ex5.3 no 2


def user_check():
    a = input('a =')
    b = input('b =')
    c = input('c =')
    n = input('n =')
    check_fermat(int(a), int(b), int(c), int(n))


# ex5.4 no 1


def is_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        print('No')
    else:
        print('Yes')


'''
ex5.4 no2
Ooops! we'll need to write another user_check() function again. I have an Idea
why don't we try to wirte a general user_check() function  that would work for any function at all
'''

# trying to generalize the user_check function


def user_check(function, par1, par2, par3):
    val0 = input('{}'.format(par1) + '=')
    val1 = input('{}'.format(par2) + '=')
    val2 = input('{}'.format(par3) + '=')
    function(int(val0), int(val1), int(val2))


user_check(is_triangle, 'h', 'i', 'j')


'''
the .format() function is how we try to handle placeholders in python. What it does is that it fills the 
empty {} with whatever par1 would be. at the end of the day what we would have in {} would be a string
OK! so this totally works! but this function would only work for a function object that has only 3 parameters
It's not so general afterall. can we still improve on it? I think I have another idea
'''


def general_user_check(function, *params):
    new_params = list()
    for param in params:
        new_params.append(int(input('{}'.format(param) + '=')))
    function(*new_params)


general_user_check(check_fermat, 'h', 'i', 'j', 'k')

'''Oh wow! this definitely works and guess what? It's totally general.
*params takes all the parameters and puts them in a list, so we can have as many parameters as possible
in the second code line a new list new_params is created. So we iterate through the list of parameters in params, 
remember params? and get it formatted in the input function. Notice that we called the int function on the input 
function. This is totally allowed in python. The * in front of the new_params in the last line of code unpacks the list
 new_params.
'''