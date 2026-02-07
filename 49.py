# 49. Feature Importance Normalizer
n = int(input("Enter number of features: "))
d = {}

for _ in range(n):
    k = input("Enter feature name: ")
    v = float(input("Enter importance value: "))
    d[k] = v

total = sum(d.values())

normalized = {k: v/total for k, v in d.items()}

print("Normalized feature importances:")
print(normalized)
