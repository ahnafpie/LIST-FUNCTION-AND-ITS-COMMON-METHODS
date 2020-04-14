# calculate the absolute difference between the sums of a square matrix diagonals.

R = int(input())
matrix = []
for i in range(R):
    matrix.append(list(map(int, input().split())))
r1, r2 = 0, 0
for i in range(R):
    r1 += matrix[i][R - i - 1]
    r2 += matrix[i][i]
print(abs(r1 - r2))
