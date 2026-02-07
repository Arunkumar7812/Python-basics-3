def remove_items(data,rem):
    return [x for x in data if x not in rem]# 23. Remove Elements Based on Another List
data = list(map(int, input("Enter data elements separated by space: ").split()))
remove_list = list(map(int, input("Enter remove_list elements separated by space: ").split()))

result = []
for x in data:
    if x not in remove_list:
        result.append(x)

print("Result after removal:", result)
