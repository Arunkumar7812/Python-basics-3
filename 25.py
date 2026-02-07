# 25. Check Row Uniqueness
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

all_rows_unique = True

for row in matrix:
    if len(row) != len(set(row)):
        all_rows_unique = False
        break

if all_rows_unique:
    print("Each row contains only unique elements")
else:
    print("At least one row contains duplicate elements")
