# 19. Reverse Dictionary Mapping
n = int(input("Enter number of items: "))

d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

# Reverse the dictionary
rev = {}

for k, v in d.items():
    rev[v] = k

print("Original dictionary:", d)
print("Reversed dictionary:", rev)