def lcis(arr):
    m=c=1
    for i in range(1,len(arr)):
        c = c+1 if arr[i]==arr[i-1]+1 else 1
        m=max(m,c)
    return m
