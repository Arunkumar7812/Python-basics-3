# 40. Dataset Consistency Checker
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

keys = set(records[0].keys())
consistent = True

for r in records:
    if set(r.keys()) != keys:
        consistent = False
        break

if consistent:
    print("Dataset is Consistent")
else:
    print("Dataset is Not Consistent")
