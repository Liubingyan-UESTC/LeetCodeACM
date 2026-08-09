# Problem: Two Sum
#
# Description:
# Given an array of integers and a target value, find two distinct indices i and j such that
# nums[i] + nums[j] == target. Return the indices in ascending order.
#
# Input:
# The first line contains an integer n (2 <= n <= 10^5), the number of elements in the array.
# The second line contains n integers nums[i], where each value satisfies -10^9 <= nums[i] <= 10^9.
# The third line contains a single integer target, where -10^9 <= target <= 10^9.
#
# Output:
# If a valid pair exists, print the two indices i and j (0-based) separated by a space, with i < j.
# If multiple pairs exist, print the pair with the smallest i; if still tied, the smallest j.
# If no such pair exists, print "-1 -1".
#
# Example:
# Input:
# 4
# 2 7 11 15
# 9
# Output:
# 0 1
#
# Note:
# This problem is intended for ACM-style input/output handling and should be solved with O(n) time complexity.

import sys
input = sys.stdin.readline

def combination_sum():
    n = int(input())
    nums = list(map(int , input().split()))
    target = int(input())

    target_map = {}

    for i , elm in enumerate(nums):
        cur = target - elm
        if cur in target_map:
            return i , target_map[cur]
        else:
            target_map[elm] = i
    
    return -1 , -1

def main():
    print(combination_sum())
