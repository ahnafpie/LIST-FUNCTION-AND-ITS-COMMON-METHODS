def FibRecursion(a):
    if a <= 1:
        return a
    else:
        return FibRecursion(a - 1) + FibRecursion(a - 2)


def fibonacci(b):
    result = []
    for i in range(b):
        result.append(FibRecursion(i))
    return result


n = int(input("Enter Series Range: "))
print("Fibonacci Series:", *fibonacci(n))
