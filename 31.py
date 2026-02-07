# 31. Vocabulary Builder
n = int(input("Number of sentences: "))
vocab = set()

for _ in range(n):
    words = input().lower().split()
    vocab.update(words)

print(vocab)
