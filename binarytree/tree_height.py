import sys
from typing import List
input = sys.stdin.readline

def build_tree(grid : List[List[int]] , start_node : int , end_node : int):
    if (0 < start_node < len(grid)) and (0 < end_node < len(grid)):
        grid[start_node - 1][end_node - 1] = 1
        grid[end_node - 1][start_node - 1] = 1

    return grid

def find_height(grid : List[List[int]] , root : int , cur_height : int):
    height = cur_height
    for i in range(root , len(grid)):
        for j in range(i , len(grid[i])):
            if grid[i][j]:
                height = max(find_height(grid , j , cur_height+1) , height)
    return height

def find_path_length(grid : List[List[int]] , tar : int , cur_len : int):
    for i in range(tar):
        if grid[tar][i]:
            if i == 0:
                return cur_len + 1
            return find_path_length(grid , i , cur_len + 1)

def main():
    # grid = [
    #     [0,1,1,0],
    #     [1,0,0,1],
    #     [1,0,0,0],
    #     [0,1,0,0]
    # ]
    # print(find_path_length(grid , 3 , 0))
    # print(find_height(grid , 0 , 0))
    n , q = tuple(map(int , input().split()))
    grid = [[0 for _ in range(n)] for _ in range(n)]
    querys = []

    for i in range(n - 1):
        s , e = tuple(map(int , input().strip()))
        grid = build_tree(grid , s , e)

    for j in range(q):
        querys.append(int(input()))

    for qu in querys:
        print(*(find_path_length(grid , qu , 0) , find_height(grid , qu , 0)))

if __name__ == "__main__":
    main()