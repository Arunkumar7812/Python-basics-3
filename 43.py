def find_duplicate_records(data):
    seen=set(); dup=[]
    for d in data:
        t=tuple(sorted(d.items()))
        if t in seen: dup.append(d)
        seen.add(t)
    return dup
