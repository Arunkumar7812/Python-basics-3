def is_cyclic(a,b):
    return len(a)==len(b) and str(b) in str(a+a)
