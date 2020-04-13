# KEYWORD & NON-KEYWORD ARGUMENTS, DEFAULT & NON-DEFAULT PARAMETER
def area(a, b):  # if we defined the parameter like area(a, b = 6): here we set a default value in the area
    # function.function argument will take that value if no argument value is passed during function call. when
    # print(area(5)) will result: 30. Default parameter can not be before non-default parameter like (a = 6, b)
    result = a * b
    return result


print(area(3, 4))  # 3 and 4 are non keyword arguments

print(area(a=5, b=6))  # a and b are keyword and a = 5, b = 6 are keyword arguments


# FUNCTION WITH AN ARBITRARY NUMBER OF NON-KEYWORD ARGUMENTS
def mean(*args):
    return sum(args) / len(args)


print(mean(3, 4, 8, 9, 8, 6))  # using a list for calculating mean is using a single object / arguments; using 


# (*)asterisk we can insert many arguments as we want to.


# FUNCTION WITH AN ARBITRARY NUMBER OF KEYWORD ARGUMENTS
def mean(**kwargs):
    return kwargs


print(mean(a=1, b=5, c=7, d=6))

# returning *args will return a tuple.
# returning **kwargs will return a dictionary.
