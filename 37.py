def group_by_length(words):
    d={}
    for w in words: d.setdefault(len(w),[]).append(w)
    return d
