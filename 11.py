# 11. Tuple Swap
t = tuple(input("Enter two elements separated by space: ").split())

if len(t) != 2:
    print("Tuple must have exactly two elements")
else:
    a, b = t
    swapped = (b, a)
    print("Swapped tuple:", swapped)