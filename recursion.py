"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be:
n = 5

5 % 2 + f(5-1)
= 1 + f(4)

4 % 2 + f(4-1)
= 0 + f(3)

3 % 2 + f(3-1)
= 1 + f(3)

2 % 2 + f(2-1)
= 1 + f(1)

1 % 2 + f (1-1)
= 1 + f(4)

f(0) = 0



# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be:
4% 2 + f(4-1)
= 1 + f(4)

3 % 2 + f(3-1)
= 0 + f(3)

2 % 2 + f(2-1)
= 1 + f(3)

1 % 2 + f(1-1)
= 1 + f(1)

f(0) = 0


# TODO: 4. use the debugger to step through and see what's actually happening
def do_something(4):
    if n < 0:
        print(n ** 2)
    do_something(n - 1)

# TODO: 5. fix do_something() so that it works according to the docstring
