from typing import List

class Solution:
    def swap(self , nums: List[int] , pos_a):
        if nums[pos_a] == pos_a + 1:
            return
        if 0 < nums[pos_a] <= len(nums):
            pos_b = nums[pos_a] - 1
            if nums[pos_a] == nums[pos_b]:
                return 
            nums[pos_a] , nums[pos_b] = nums[pos_b] , nums[pos_a]
            self.swap(nums , pos_a)


    def firstMissingPositive(self, nums: List[int]) -> int:
        cur = 0
        len_nums = len(nums)
        while cur < len_nums:
            self.swap(nums , cur)

            cur += 1
        for i in range(len_nums):
            if nums[i] != i + 1:
                return i + 1
        return len_nums+1
    

if __name__ == "__main__":
    solution = Solution()
    # tests = [3,4,-1,1]
    # tests = [0 , 1 , 2]
    tests = [1 , 1]
    # tests = [-1,4,2,1,9,10]
    res = solution.firstMissingPositive(tests)
    print(res)
