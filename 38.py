def invert_dict(d):
    r={}
    for k,v in d.items(): r.setdefault(v,[]).append(k)
    return r
