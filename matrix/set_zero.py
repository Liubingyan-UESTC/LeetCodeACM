# 矩阵置零
import sys
input = sys.stdin.readline 

def set_zero(matrix):
    len_row = len(matrix)
    len_col = len(matrix[0])

    row_list = [0 for _ in range(len_row)]
    col_list = [0 for _ in range(len_col)]

    for i in range(len_row):
        for j in range(len_col):
            if matrix[i][j] == 0:
                row_list[i] = 1
                col_list[j] = 1

    for i in range(len_row):
        for j in range(len_col):
            if row_list[i] + col_list[j] > 0:
                matrix[i][j] = 0
    return matrix

def main():
    mat = [
        [1,2,3,0,3,1],
        [0,3,4,7,1,0],
        [9,9,2,3,4,6],
        [4,1,0,6,6,2],
        [8,0,2,5,3,7]
    ]
    print(set_zero(mat))

if __name__ == "__main__":
    main()