# 34. Pangram Checker
s = input().lower()
letters = set(c for c in s if c.isalpha())

if len(letters) == 26:
    print("Pangram")
else:
    print("Not Pangram")
