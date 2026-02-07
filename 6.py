rows = int(input("Enter number of rows: "))

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter elements of row {i+1}: ").split()))
    matrix.append(row)
z=zip(*matrix)
print("Row-wise maximums:")
for row in z:
    print(sum(row))