# 32. Duplicate Detector
arr = list(map(int, input().split()))
if len(arr) != len(set(arr)):
    print("Duplicates found")
else:
    print("No duplicates")