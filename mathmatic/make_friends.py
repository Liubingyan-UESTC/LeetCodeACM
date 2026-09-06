# 找朋友
import sys
input = sys.stdin.readline 


def make_friends(class_A , class_B , M):
    a = sorted(student % M for student in class_A)
    b = sorted(student % M for student in class_B)

    len_a = len(a)

    base_sum = sum(a) + sum(b)

    i , j = 0 , len_a - 1

    overflow_count = 0

    while i < len_a and j >= 0:
        if a[i] + b[j] >= M:
            overflow_count += 1
            i += 1
            j -= 1
        else:
            i += 1
    min_sum = base_sum - (overflow_count * M)
    return min_sum


def main():
    T = int(input().strip())
    class_A = []
    class_B = []
    num_students = []
    Ms = []
    for i in range(T):
        n , m = tuple(map(int , input().split()))
        a = list(map(int , input().strip().split()))
        b = list(map(int , input().strip().split()))
        class_A.append(a)
        class_B.append(b)
        num_students.append(n)
        Ms.append(m)

    for times in range(T):
        print(make_friends(class_A[times] , class_B[times] , Ms[times]))


if __name__ == "__main__":
    main()