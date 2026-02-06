arr = list(map(int, input("Enter the elements: ").split()))

result = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        result.append(arr[i])

print("After removing consecutive duplicates:", result)
