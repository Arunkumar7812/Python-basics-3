# 33. Skill Gap Analyzer
required = set(input("Required skills: ").split())
student = set(input("Student skills: ").split())

missing = required - student
extra = student - required

print("Missing skills:", missing)
print("Extra skills:", extra)