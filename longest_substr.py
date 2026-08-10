# 无重复字符的最长子串
import sys
input = sys.stdin.readline
MAX_N= 26

def longest_substr(s : str) -> int:
    len_s = len(s)
    if len_s == 0:
        return 0
    l , r = 0 , 0
    max_len = 0
    cur_len = 0
    count = [0 for _ in range(MAX_N)]
    while r < len_s:
        if count[ord(s[r]) - ord('a')] == 0:    # 当前字符没有出现过
            count[ord(s[r]) - ord('a')] += 1
            cur_len += 1
            r += 1
        else:
            while s[l] != s[r]:
                count[ord(s[l]) - ord('a')] -= 1
                l += 1
                cur_len -= 1
            count[ord(s[l]) - ord('a')] -= 1
            l += 1
            cur_len -= 1
        max_len = max(max_len , cur_len)
    
    return max_len

def main():
    s = input().strip()
    print(longest_substr(s))




