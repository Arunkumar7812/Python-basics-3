rows = int(input("Enter number of rows: "))
matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)

for row in matrix:
    print(max(row))
