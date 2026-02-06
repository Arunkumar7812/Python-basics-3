def co_occurrence(sentence):
    w=sentence.split()
    d={}
    for i in range(len(w)-1):
        p=(w[i],w[i+1])
        d[p]=d.get(p,0)+1
    return d
