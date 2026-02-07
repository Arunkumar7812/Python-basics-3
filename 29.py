# 29. Tuple Frequency Counter
n = int(input("Enter number of tuples: "))
tuples_list = []

for _ in range(n):
    a, b = map(int, input("Enter tuple (a b): ").split())
    tuples_list.append((a, b))

freq = {}
for t in tuples_list:
    freq[t] = freq.get(t, 0) + 1

print(freq)