import sys
from typing import List
input = sys.stdin.readline

def merge(ranges : List[List[int]]):
    if not ranges : 
        return 0 , 0 , 0
    num_res = 0
    sum_len = 0
    max_len = 0

    ranges = sorted(ranges , key = lambda x:x[0])

    merged = [ranges[0][:]]

    for start , end in ranges[1:]:
        last_start , last_end = merged[-1]

        if start <= last_end:
            merged[-1][1] = max(end, last_end)

        else:
            merged.append([start , end])

    num_res = len(merged)    

    for intervals in merged:
        sum_len += (intervals[1] - intervals[0])
        max_len = max(max_len , intervals[1] - intervals[0])

    return num_res , sum_len , max_len


def main():
    n = int(input().strip())
    ranges = []
    for i in range(n):
        ranges.append(
            list(map(int , input().split()))
        )
    print(*merge(ranges))


if __name__ == "__main__":
    main()
