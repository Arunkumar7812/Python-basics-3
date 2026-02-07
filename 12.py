# 12. Tuple-Based Statistics
nums=list(map(int,input().split()))
mini=min(nums)
maxi=max(nums)
avg=sum(nums)/len(nums)
t=(mini,maxi,avg)
print(t)