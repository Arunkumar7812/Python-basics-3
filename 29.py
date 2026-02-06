def tuple_freq(lst):
    d={}
    for t in lst: d[t]=d.get(t,0)+1
    return d
