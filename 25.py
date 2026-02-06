def row_unique(mat):
    return all(len(r)==len(set(r)) for r in mat)
