# 43. Duplicate Record Identifier
n = int(input("Enter number of records: "))
records = []

for i in range(n):
    m = int(input(f"Enter number of key-value pairs in record {i+1}: "))
    d = {}
    for _ in range(m):
        k = input("Enter key: ")
        v = input("Enter value: ")
        d[k] = v
    records.append(d)

seen = set()
duplicates = []

for r in records:
    t = tuple(sorted(r.items()))
    if t in seen:
        duplicates.append(r)
    else:
        seen.add(t)

print("Duplicate records found:")
print(duplicates)
