# 44. Word Co-Occurrence Counter
sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}

for i in range(len(words) - 1):
    pair = (words[i], words[i+1])
    freq[pair] = freq.get(pair, 0) + 1

print("Word co-occurrence counts:")
print(freq)
