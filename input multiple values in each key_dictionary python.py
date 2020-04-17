d = {}
name, *line = input().split()
s = list(map(float, line))
d[name] = s
print(d)

# Sample input: a 1 2 3
# Sample_output: {'a': [1.0, 2.0, 3.0]}
