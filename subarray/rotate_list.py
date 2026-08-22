# 轮转数组
import sys
input = sys.stdin.readline 

def rotate_inplace(nums):
    """
    轮转整个数组
    """
    nums[:] = nums[::-1]

def rotate(nums , lens):
    lens = lens % len(nums)
    rotate_inplace(nums)
    nums[:lens] = nums[:lens][::-1]
    nums[lens:] = nums[lens:][::-1]

    return nums

def main():
    nums = [1,2,3,4,5,6,7]
    lens = 3
    print(rotate(nums , lens))

main()


# NOTE : 轮转数组需要考虑操作是原地操作还是创建了一个新的对象