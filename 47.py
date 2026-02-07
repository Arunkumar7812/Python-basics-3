# 47. Ranking with Tie Handling
scores = list(map(int, input("Enter scores in descending order separated by space: ").split()))

ranks = []
rank = 1

for i in range(len(scores)):
    if i > 0 and scores[i] == scores[i-1]:
        ranks.append(rank)
    else:
        rank = i + 1
        ranks.append(rank)

print("Ranks:", ranks)
