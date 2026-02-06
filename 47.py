def assign_ranks(scores):
    r=[]; rank=1; prev=None; skip=0
    for s in sorted(scores,reverse=True):
        if s!=prev: rank+=skip; skip=0
        r.append(rank); skip+=1; prev=s
    return r
