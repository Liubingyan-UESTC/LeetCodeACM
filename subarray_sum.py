# 和为k的子数组
import sys
input = sys.stdin.readline

def subarray_sum(nums : list[int] , k : int) -> int:
    len_nums = len(nums)
    prefix_sum = [0 for _ in range(len_nums + 1)]
    prefix_sum[0] = 0
    for i in range(1 , len_nums + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    
    count = 0

    for i in range(len_nums + 1):
        for j in range(i + 1 , len_nums + 1):
            if prefix_sum[j] - prefix_sum[i] == k:
                count += 1
    
    return count

def main():
    nums = list(map(int , input().strip().split()))
    k = int(input().strip())
    print(subarray_sum(nums , k))
