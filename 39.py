from collections import Counter
def top_k(lst,k):
    return [x for x,_ in Counter(lst).most_common(k)]
