# 50. Dataset Summary Generator
n = int(input("Enter number of records (rows): "))
records = []

for i in range(n):
    m = int(input(f"Enter number of fields in record {i+1}: "))
    d = {}
    for _ in range(m):
        k = input("Enter field name: ")
        v = input("Enter field value: ")
        d[k] = v
    records.append(d)

summary = {"rows": len(records), "unique_values": {}}

keys = records[0].keys()
for k in keys:
    values = set(r[k] for r in records)
    summary["unique_values"][k] = len(values)

print("Dataset summary:")
print(summary)
