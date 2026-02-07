#18. Student Average Calculator
n = int(input("Enter number of students: "))

students = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    students[name] = marks

averages = {}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    averages[name] = avg

print("Average marks of each student:")
print(averages)
