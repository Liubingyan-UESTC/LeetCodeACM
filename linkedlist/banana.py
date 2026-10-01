

from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    len_p = len(piles)
    min_speed = 1
    max_speed = max(piles)

    for speed in range(min_speed , max_speed+1):
        temp = piles[:]
        cur_idx = 0
        i = 0
        while i < h:
            if temp[cur_idx] == 0:
                cur_idx = (cur_idx + 1) % len_p
            elif temp[cur_idx] < speed:
                temp[cur_idx] = 0
                cur_idx = (cur_idx + 1) % len_p
                i += 1
            else:
                temp[cur_idx] -= speed
                cur_idx = (cur_idx + 1) % len_p
                i += 1
        if max(temp) <= 0:
            return speed

def main():
    piles = [30,11,23,4,20]
    h = 8
    return minEatingSpeed(piles , h)

if __name__ == "__main__":
    main()
