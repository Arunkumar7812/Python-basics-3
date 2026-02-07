n = int(input("Enter number of rows: "))

nums=[]
for i in range(n):
  row = list(map(int, input(f"Enter row {i+1}: ").split()))
  nums.append(row)

l=[]
for i in nums:
  for j in i:
    l.append(j)
print(l)