# 17. Symmetric Difference
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in l1:
  if not i in l2 :
    l.append(i)
for i in l2:
  if not i in l1 :
    l.append(i)
print(l)