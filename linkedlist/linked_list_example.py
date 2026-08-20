import sys

from templates.linked_list import ListNode

input = sys.stdin.readline


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # 1) 用模板构造链表
    head = ListNode().create(nums[:n], head_insert=False)

    # 2) 以示例方式操作链表：在中间插入一个节点
    if head is None:
        print()
        return
    if head.next is not None:
        head.insert_after(head.next, 99)
    else:
        head.insert_after(head, 99)

    # 3) 删除尾节点，展示 delete_node 的用法
    cur = head
    while cur.next is not None:
        cur = cur.next
    head = head.delete_node(cur)

    # 4) 输出最终链表
    print(*head.to_list())


if __name__ == "__main__":
    main()
