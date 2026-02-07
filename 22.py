# 22. Split List by Condition
nums=list(map(int,input().split()))
even=[x for x in nums if x%2==0]
odd=[x for x in nums if x%2==1]
print(odd)
print(even)