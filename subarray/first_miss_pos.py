# 缺失的第一个正数
import sys
input = sys.stdin.readline 

def first_miss(nums: list) -> int:
    len_nums = len(nums)
    cur = 0
    while cur < len_nums:
        if nums[cur] == cur + 1:
            cur += 1
            continue
        else:
    return 0