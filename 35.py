# 35. Highest Value Key
n = int(input("Enter number of key-value pairs: "))
d = {}

for _ in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

max_key = max(d, key=d.get)
print("Key with highest value:", max_key)
