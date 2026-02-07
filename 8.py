nums = list(map(int, input("Enter numbers: ").split()))

leaders = []
max_so_far = float('-inf')

for i in range(len(nums)-1, -1, -1):
    if nums[i] > max_so_far:
        leaders.append(nums[i])
        max_so_far = nums[i]

leaders.reverse()

print("Leader elements:", leaders)