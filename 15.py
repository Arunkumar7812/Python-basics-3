l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
l=[]
for i in l1:
  if i in l2 and i in l3 and not i in l:
    l.append(i)
print(l)