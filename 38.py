# 38. Invert Dictionary with List Values
n = int(input("Enter number of students: "))
d = {}

for _ in range(n):
    student = input("Enter student name: ")
    dept = input("Enter department: ")
    d[student] = dept

inv = {}
for student, dept in d.items():
    if dept not in inv:
        inv[dept] = []
    inv[dept].append(student)

print("Inverted dictionary (dept -> students):", inv)
