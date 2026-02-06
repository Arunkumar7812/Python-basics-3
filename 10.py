names = input("Enter student names: ").split()
marks = list(map(int, input("Enter marks: ").split()))

# Pair names and marks
students = list(zip(names, marks))

# Sort by marks (descending)
students.sort(key=lambda x: x[1], reverse=True)

rank = 1
prev_marks = None
count = 0

for name, mark in students:
    count += 1
    if mark != prev_marks:
        rank = count
    print(name, "→ Rank", rank)
    prev_marks = mark
