# 42. Department-wise Topper
n = int(input("Enter number of students: "))
students = []

for _ in range(n):
    name = input("Enter student name: ")
    dept = input("Enter department: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "dept": dept, "marks": marks})

top = {}

for s in students:
    d = s["dept"]
    if d not in top or s["marks"] > top[d]["marks"]:
        top[d] = s

print("Topper in each department:")
print(top)
