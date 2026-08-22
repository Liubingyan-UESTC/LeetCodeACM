# 合并区间

import sys
input = sys.stdin.readline

def merge_intervals(intervals:list[list]) -> list:
    len_int = len(intervals)

    intervals.sort(key = lambda x : x[0])
    res = []
    for i in range(len_int):
        if i == 0:
            res.append(intervals[i])
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1] , intervals[i][1])
        else:
            res.append(intervals[i])
    return res

def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        s = list(map(int , input().split()))
        intervals.append(s)
    print(merge_intervals(intervals))

if __name__ == "__main__":
    main()