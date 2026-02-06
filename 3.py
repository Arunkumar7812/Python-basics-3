nums = list(map(int, input("Enter numbers: ").split()))
K = int(input("Enter K: "))

freq = {}
count = 0

for n in nums:
    if K - n in freq:
        count += freq[K - n]
    freq[n] = freq.get(n, 0) + 1

print("Number of pairs:", count)
