# 36. Merge Dictionaries with Sum
n = int(input("Enter number of keys: "))

d1 = {}
d2 = {}

print("Enter first dictionary:")
for _ in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d1[k] = v

print("Enter second dictionary:")
for _ in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d2[k] = v

merged = {}
for k in d1:
    merged[k] = d1[k] + d2[k]

print("Merged dictionary with summed values:", merged)
