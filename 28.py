# 28. Sort Tuple List by Second Element
n = int(input("Enter number of students: "))

data = []
for i in range(n):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    data.append((name, score))
sorted_data=sorted(data,key=lambda x : x[1],reverse=True)

print(sorted_data)