r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

matrix = []
for i in range(r):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)

col_sum = [0] * c

for i in range(r):
    for j in range(c):
        col_sum[j] += matrix[i][j]

print("Column sums:", col_sum)
