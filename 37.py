# 37. Word Length Grouping
words = input("Enter words separated by space: ").split()
groups = {}

for w in words:
    l = len(w)
    if l not in groups:
        groups[l] = []
    groups[l].append(w)

print("Words grouped by length:", groups)