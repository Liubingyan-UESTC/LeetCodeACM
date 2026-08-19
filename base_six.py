import sys
input = sys.stdin.readline
INT_BIT = 32

def step_in(num_list , cur_p):
    while num_list[cur_p] == 6:
        num_list[cur_p] = 0
        cur_p -= 1
        num_list[cur_p] += 1

def main():
    num = int(input().strip())
    negtive = False
    # num_list = [0 for _ in range(INT_BIT)]
    # cur_p = INT_BIT - 1
    # if num < 0:
    #     negtive = True
    # num = abs(num)

    # for i in range(num):
    #     num_list[cur_p] += 1
    #     if num_list[cur_p] == 6:
    #         step_in(num_list , cur_p)
    
    # while num_list and num_list[0] == 0:
    #     num_list.pop(0)
    # if not num_list:
    #     print(0)
    # else:
    #     s = int("".join(map(str,num_list)))

    # print(-1 * s if negtive else s)
    if num < 0:
        negtive = True
    sign = "-" if negtive else ""
    num = abs(num)
    temp = num
    res = ""
    while temp > 0:
        val = temp // 6
        left = temp % 6
        res = str(left) + res
        if val == 0:
            break

        temp = val
    print(sign +"".join(res))
main()
