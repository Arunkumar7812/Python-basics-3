num=list(map(int, input("Enter the nimbers:").split()))
freq={}
for n in num:
    freq[n] = freq.get(n,0) + 1
    
result = []
for n in num:
    if freq[n] == 1:
        result.append(n)
print(result)
    