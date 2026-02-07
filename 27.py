# 27. Cyclic Shift Equality
a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

if len(a) != len(b):
    print("Not cyclic rotations")
else:
    a2 = a + a
    found = False
    for i in range(len(a)):
        if a2[i:i+len(b)] == b:
            found = True
            break

    if found:
        print("Yes, second list is a cyclic rotation of the first")
    else:
        print("No, they are not cyclic rotations")