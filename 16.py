# 16. Missing Digits
num=input("Enter Number : ")
missing_digits=[]
for i in range(10):
  a=str(i)
  if a not in num:
    missing_digits.append(i)
print(missing_digits)