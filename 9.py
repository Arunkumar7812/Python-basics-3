nums=list(map(int,input().split()))
l=[]
for i in range(len(nums)-1):
  if nums[i]!=nums[i+1]:
    l.append(nums[i])
l.append(nums[-1])
print(l)