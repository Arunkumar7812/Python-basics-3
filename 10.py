# 10. Rank Students
names = input("Enter names (space separated): ").split()
marks = list(map(int, input("Enter marks (space separated): ").split()))

# Combine names and marks
students = list(zip(names, marks))

# Sort by marks in descending order
students.sort(key=lambda x: x[1], reverse=True)

print("Rank  Name")
rank = 1
for name, mark in students:
    print(rank , name)
    rank += 1
