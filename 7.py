nested = eval(input("Enter the nested list: "))
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print("Flattened list:", flat)
