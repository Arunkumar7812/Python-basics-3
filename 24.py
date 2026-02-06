def diag_sum(m):
    n=len(m)
    return sum(m[i][i] for i in range(n)), sum(m[i][n-i-1] for i in range(n))
