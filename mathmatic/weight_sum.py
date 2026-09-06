import sys
input = sys.stdin.readline 
MAX_NUM = 10e9 + 7

def w_sum(lists : list):
    len_l = len(lists)
    res = [0]
    for i in range(1,len_l):
        cur_sum = 0
        for j in range(len_l):
            cur_sum += (j % (i+1)) * lists[j]
        res.append(int(cur_sum % MAX_NUM))
    sys.stdout.write(" ".join(map(str , res)))

def main():
    T = int(input())
    lens = []
    lists = []

    for i in range(T):
        n = int(input().strip())
        lens.append(n)
        lists.append(list(map(int , input().strip().split())))

    for elm in lists:
        w_sum(elm)
        print()

if __name__ == "__main__":
    main()
