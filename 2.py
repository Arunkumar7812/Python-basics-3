num=list(map(int, input("Enter the numbers:").split()))
res=[]
for i in num:
    if num.count(i)==1:
        res.append(i)
print(res)