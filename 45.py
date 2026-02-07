# 45. Resume Skill Match Score
n = int(input("Enter number of required skills: "))
required = {}

for _ in range(n):
    skill = input("Enter skill name: ")
    weight = int(input("Enter weight for this skill: "))
    required[skill] = weight

m = int(input("Enter number of candidate skills: "))
candidate = {}

for _ in range(m):
    skill = input("Enter skill name: ")
    prof = int(input("Enter proficiency level: "))
    candidate[skill] = prof

score = 0
for skill in required:
    if skill in candidate:
        score += required[skill] * candidate[skill]

print("Resume match score:", score)
