# 30. Pair Formation Using Tuples
nums = list(map(int, input().split()))
result = [(x, x*x) for x in nums]
print(result)