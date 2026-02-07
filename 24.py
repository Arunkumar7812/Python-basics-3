# 24. Diagonal Sum of Matrix
n = int(input("Enter size of matrix (n): "))

matrix = []
print("Enter the matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - 1 - i]

print("Primary diagonal sum:", primary_sum)
print("Secondary diagonal sum:", secondary_sum)