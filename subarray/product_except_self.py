# 除自身以外的数组乘积
import sys
input = sys.stdin.readline 

def prefix_product(nums : list) -> list:
    cur_pro = 1
    len_nums = len(nums)
    prefix_res = [1]
    for i in range(1,len_nums):
        cur_pro *= nums[i-1]
        prefix_res.append(cur_pro)

    return prefix_res

def product_except_self(nums):
    pref = prefix_product(nums)
    suff = prefix_product(nums[::-1])[::-1]    # 这里要把后缀翻转过来
    res = []
    for i in range(len(nums)):
        res.append(pref[i] * suff[i])
    return res

def main():
    nums = [1,2,3,4]
    print(product_except_self(nums))

if __name__ == "__main__":
    main()





