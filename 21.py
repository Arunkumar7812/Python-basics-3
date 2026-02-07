# 21. Longest Consecutive Increasing Subsequence
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

if n == 0:
    print(0)
else:
    curr_len = 1
    max_len = 1
    for i in range(1,n):
      if nums[i]>nums[i-1]:
        curr_len+=1
      else:
        curr_len=1
      if curr_len>max_len:
        max_len=curr_len
print("Longest Consecutive Increasing Subsequence Length : ",max_len)