nums = list(map(int, input("Enter numbers: ").split()))
K = int(input("Enter K: "))

n = len(nums)
K = K % n   # handles K > n

rotated = nums[-K:] + nums[:-K]
print(rotated)
