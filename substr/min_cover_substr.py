# 最小覆盖子串
import sys
input = sys.stdin.readline
VOCAB_SIZE = 26

def build_hash_list(s) -> list:
    hash_list = [0 for _ in range(VOCAB_SIZE)]
    for elm in s:
        hash_list[ord(elm) - ord("a")] += 1
    return hash_list

def is_cover(s:list , t:list):
    for i in range(VOCAB_SIZE):
        if s[i] < t[i]:
            return False
    return True

    

def min_cover(s , t) -> str:
    len_s = len(s)
    len_t = len(t)
    if len_s < len_t:
        return ""
    

    t_hash = build_hash_list(t)
    l = 0
    r = 0
    cur_start = 0
    cur_min = len_s + 1
    s_hash = [0 for _ in range(VOCAB_SIZE)]
    while r < len_s:
        s_hash[ord(s[r]) - ord("a")] += 1
        while is_cover(s_hash , t_hash):
            if r - l + 1 < cur_min:
                cur_min = r - l + 1
                cur_start = l
            
            s_hash[ord(s[l]) - ord("a")] -= 1
            l += 1
        r += 1
    return s[cur_start : cur_start + cur_min]

def main():
    # s = input().strip()
    # t = input().strip()
    s = "ADOBECODEBANC".lower()
    t = "ABC".lower()
    print(min_cover(s , t))

if __name__ == "__main__":
    main()
