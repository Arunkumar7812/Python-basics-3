# 39. Top K Frequent Elements
from collections import Counter

arr = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter value of K: "))

freq = Counter(arr)
topk = freq.most_common(k)

result = [x[0] for x in topk]
print("Top K frequent elements:", result)
