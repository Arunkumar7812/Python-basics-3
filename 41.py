# 41. Student Performance Index
n = int(input("Enter number of students: "))
students = []

for _ in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance: "))
    students.append({"name": name, "marks": marks, "attendance": attendance})

index = {}

for s in students:
    score = s["marks"] * 0.7 + s["attendance"] * 0.3
    index[s["name"]] = score

topper = max(index, key=index.get)

print("Performance index of students:", index)
print("Topper:", topper)
