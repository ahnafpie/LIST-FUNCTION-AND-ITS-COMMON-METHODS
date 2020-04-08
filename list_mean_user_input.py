def mean(value):
    x = sum(value) / len(value)
    return x


s = input("Enter Values: ")
user_input = list(map(float, s.split()))
print("Mean =", mean(user_input))
