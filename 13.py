# 13. Unique Tuple Pairs
n=int(input("Enter number of elements: "))
pairs=[]
for i in range(n):
  a,b=map(int,input().split())
  pairs.append((a,b))
seen=set()
result=[]

for a,b in pairs:
  normalised=tuple(sorted((a,b)))
  if normalised not in seen :
    seen.add(normalised)
    result.append((a,b))
print(result)
