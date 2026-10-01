import sys
input = sys.stdin.readline 

a = [
    [1,2,3,4,5],
    [2,12,4,3,11],
    [12,3,1,1,0],
]
b = [
    [1,0,2],
    [2,12,8],
    [5,4,12],
    [1,0,1],
    [2,2,2]
]

def mat_mul(a , b):
    row_a = len(a)
    col_a = len(a[0])

    row_b = len(b)
    col_b = len(b[0])

    res = [[0 for _ in range(col_b)] for _ in range(row_a)]

    if col_a != row_b:
        print("dim don't match")
        return None

    for i in range(row_a):
        ai = a[i]
        for j in range(col_b):
            bj = b[:,j]
            for k in range(col_a):
                res[i][j] += ai[k] * bj[k]
    return res

