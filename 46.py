# 46. Vocabulary Coverage Analyzer
expected = set(input("Enter expected vocabulary words (space separated): ").split())
docs = input("Enter document text: ").lower().split()

doc_set = set(docs)

covered = expected & doc_set
missing = expected - doc_set

percentage = (len(covered) / len(expected)) * 100

print("Vocabulary coverage percentage:", percentage)
print("Missing words:", missing)
