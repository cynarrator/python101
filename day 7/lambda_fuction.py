def sum(a, b):
    return a + b

# print(sum(1, 2))

def myFunc(n):
    """
    Returns lambda a: a * n
    Where n is passed in from wrapper myFunc
    and a is later passed to lambda
    """
    return lambda a: a * n


my_doubler = myFunc(2)
print(my_doubler(3))