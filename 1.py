num = list(map(int, input("Enter numbers:").split()))
if len(num)<2:
    print("Second minimum is not possible")
else:
    min1 = min2 =float('inf')
    
    for n in num:
        if n <min1:
            min2 = min1
            min1 = n
        elif min1 <n< min2:
            min2=n
    if min2 == float('inf'):
        print("Second minimum is not found")
    else:
        print("Second Minimum:",min2)