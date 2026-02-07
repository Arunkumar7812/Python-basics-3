# 14. Unique Word Counter
words=input().split()
s=set()
for i in words:
  if i not in s:
    s.add(i)
print(s)