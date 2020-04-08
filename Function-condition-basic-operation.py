"""here we define a function name  mean  and  'mylist' works as the  variable.
then we declared the mean algorithm and returned  the  output on x. here y is
a list. when we put it into the mean function it acts as mylist. an arbitrary
variable  like 'x'  was  declared and  returned the  output. the value  of  a
is always what you return. always use return in your function"""


def mean(mylist):
    x = sum(mylist) / len(mylist)
    return x


y = [2, 3, 4, 5, 6, 7]

print(mean(y))

'''this function works only for list type. now we will set it to works for both
list and dict type by using if_else conditional.'''


def mean(value):
    if type(value) == dict:
        x = sum(value.values()) / len(value)
    else:
        x = sum(value) / len(value)
    return x


y = [2, 3, 4, 5, 6, 7]
print(mean(y))

z = {'K': 4, 'h': 5, 'l': 6}
print(mean(z))

''' "isinstance also return the same output. It is more recommended to use'''


def mean(value):
    if isinstance(value, dict):
        x = sum(value.values()) / len(value)
    else:
        x = sum(value) / len(value)
    return x


y = [2, 3, 4, 5, 6, 7]
print(mean(y))

z = {'K': 4, 'h': 5, 'l': 6}
print(mean(z))

'''elif conditional'''

a = 90
b = 90
if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a is equal to b")

'''result squally:
 4.5
4.5
5.0
4.5
5.0
a is equal to b'''
