# 滑动窗口最大值
import sys
from collections import deque
input = sys.stdin.readline

def max_sliding_window(nums : list , k : int) -> list:
    # 暴力解 O(n*k)
    # res = []
    # for i in range(len(nums) - k + 1):
    #     res.append(max(nums[i : i + k]))
    # return res

    # 单调递减队列 O(n)：队列中存下标，队首永远是窗口最大值
    dq = deque()
    res = []
    for i , x in enumerate(nums):
        # 队首下标滑出窗口，移出
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        # 窗口形成后，队首即当前窗口最大值
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

def main():
    # nums = list(map(int , input().strip().split()))
    # k = int(input().strip())
    nums = [100 , 23, 44, 5554, 4454, 345, 4343 ,233 ,324]
    k= 3
    print(max_sliding_window(nums , k))

if __name__ == "__main__":
    main()