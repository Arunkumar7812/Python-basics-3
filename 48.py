# 48. Configuration Validator
n = int(input("Enter number of configuration entries: "))
config = {}

for _ in range(n):
    k = input("Enter config key: ")
    v = input("Enter config value: ")
    config[k] = v

required = set(input("Enter required keys (space separated): ").split())

missing = required - config.keys()
extra = config.keys() - required

print("Missing keys:", missing)
print("Extra keys:", extra)
