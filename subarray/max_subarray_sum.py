# 最大子数组和
import sys
input = sys.stdin.readline

# 暴力
def max_sum_dir(nums: list) -> int:
    len_nums = len(nums)
    max_sum = float("-inf")
    for i in range(len_nums):
        cur_sum = 0
        for j in range(i , len_nums):
            cur_sum += nums[j]
            max_sum = max(max_sum , cur_sum)
    return int(max_sum)

# dp
def max_sum_dp(nums : list) -> int:
    len_nums = len(nums)
    dp = [0 for _ in range(len_nums)]
    dp[0] = nums[0]
    for i in range(len_nums):
        dp[i] = max(dp[i- 1] + nums[i] , nums[i])
    return max(dp)

# 分治
def cross_sum(nums , low , mid , high):
    l_sum = 0
    r_sum = 0
    l_max = float("-inf")
    r_max = float("-inf")
    for i in range(mid - 1 ,low - 1, -1):
        l_sum += nums[i]
        l_max = max(l_max , l_sum)
    for j in range(mid  , high):
        r_sum += nums[j]
        r_max = max(r_max , r_sum)
    return l_max + r_max

def max_sum_div(nums:list) -> int:
    len_nums= len(nums)
    if len_nums == 1:
        return nums[0]
    edge = len_nums // 2 
    cross = cross_sum(nums , 0 , edge , len_nums)
    l = 0
    r = len_nums
    lmax_sum = max_sum_div(nums[l:edge])
    rmax_sum = max_sum_div(nums[edge:r])

    max_sum = max(lmax_sum , rmax_sum , cross)

    return int(max_sum)


    

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sum_dp(nums))
    print(max_sum_dir(nums))
    print(max_sum_div(nums))

if __name__ == "__main__":
    main()

