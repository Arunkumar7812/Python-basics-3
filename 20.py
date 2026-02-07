# 20. Character Classification Counter
s = input("Enter a string: ")

count = {
    "alphabets": 0,
    "digits": 0,
    "special_characters": 0
}

for ch in s:
    if ch.isalpha():
        count["alphabets"] += 1
    elif ch.isdigit():
        count["digits"] += 1
    else:
        count["special_characters"] += 1

print(count)