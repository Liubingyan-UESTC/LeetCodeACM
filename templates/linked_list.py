class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> list:
        """将链表转为 Python list，便于测试与调试。"""
        vals = []
        cur = self
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals

    def create(self, nums: list, head_insert: bool = True) -> "ListNode | None":
        """
        由数组创建链表。
        head_insert=True  头插法（结果顺序与 nums 相反）
        head_insert=False 尾插法（结果顺序与 nums 相同）
        """
        if not nums:
            return None
        if head_insert:  # 头插法
            virtual_head = ListNode()
            for num in nums:
                self.insert_after(virtual_head, num)
            return virtual_head.next 
        else:  # 尾插法
            virtual_head = ListNode()
            cur = virtual_head
            for num in nums:
                cur.next = ListNode(num)
                cur = cur.next
            return virtual_head.next

    def insert_after(self, node: "ListNode", val) -> None:
        """在 node 后插入值为 val 的新节点。"""
        nxt = node.next
        new_node = ListNode(val)
        new_node.next = nxt
        node.next = new_node

    def find_prev(self, node: "ListNode") -> "ListNode | None":
        """
        找到 node 的前驱节点。
        若 node 就是当前头节点，或 node 不在链表中，返回 None。
        """
        if node is self:
            return None
        cur = self
        while cur and cur.next is not node:
            cur = cur.next
        if cur is None:
            return None
        return cur

    def delete_node(self, node: "ListNode") -> "ListNode | None":
        """
        删除 node 节点，返回删除后的新头节点。
        - 删除头节点：返回原 head.next
        - 删除中间/尾节点：返回原 head
        - node 不在链表中：不做修改，返回原 head
        """
        if node is self:
            return self.next

        prev = self.find_prev(node)
        if prev is None:
            return self
        prev.next = node.next
        return self


def _assert_eq(actual, expected, msg: str) -> None:
    if actual != expected:
        raise AssertionError(f"{msg}: expected {expected!r}, got {actual!r}")
    print(f"[OK] {msg}: {actual}")


if __name__ == "__main__":
    helper = ListNode()

    # 1. 空数组
    _assert_eq(helper.create([], True), None, "create empty + head_insert")
    _assert_eq(helper.create([], False), None, "create empty + tail_insert")

    # 2. 尾插法：顺序与输入一致
    head = helper.create([1, 2, 3, 4], head_insert=False)
    _assert_eq(head.to_list(), [1, 2, 3, 4], "create tail_insert")

    # 3. 头插法：顺序与输入相反
    head = helper.create([1, 2, 3, 4], head_insert=True)
    _assert_eq(head.to_list(), [4, 3, 2, 1], "create head_insert")

    # 4. insert_after：在头节点后插入
    head = helper.create([1, 3], head_insert=False)
    head.insert_after(head, 2)
    _assert_eq(head.to_list(), [1, 2, 3], "insert_after head")

    # 5. insert_after：在中间节点后插入
    head = helper.create([1, 2, 4], head_insert=False)
    mid = head.next  # 2
    head.insert_after(mid, 3)
    _assert_eq(head.to_list(), [1, 2, 3, 4], "insert_after middle")

    # 6. find_prev：头节点无前驱
    head = helper.create([1, 2, 3], head_insert=False)
    _assert_eq(head.find_prev(head), None, "find_prev of head")

    # 7. find_prev：中间 / 尾节点
    node2 = head.next
    node3 = head.next.next
    _assert_eq(head.find_prev(node2) is head, True, "find_prev of middle")
    _assert_eq(head.find_prev(node3) is node2, True, "find_prev of tail")

    # 8. find_prev：节点不在链表中
    outsider = ListNode(99)
    _assert_eq(head.find_prev(outsider), None, "find_prev missing node")

    # 9. delete_node：删除中间节点
    head = helper.create([1, 2, 3, 4], head_insert=False)
    node2 = head.next
    head = head.delete_node(node2)
    _assert_eq(head.to_list(), [1, 3, 4], "delete middle")

    # 10. delete_node：删除尾节点
    head = helper.create([1, 2, 3], head_insert=False)
    tail = head.next.next
    head = head.delete_node(tail)
    _assert_eq(head.to_list(), [1, 2], "delete tail")

    # 11. delete_node：删除头节点
    head = helper.create([1, 2, 3], head_insert=False)
    head = head.delete_node(head)
    _assert_eq(head.to_list(), [2, 3], "delete head")

    # 12. delete_node：只剩一个节点
    head = helper.create([1], head_insert=False)
    head = head.delete_node(head)
    _assert_eq(head, None, "delete sole node")

    # 13. delete_node：目标不在链表中，链表不变
    head = helper.create([1, 2, 3], head_insert=False)
    head = head.delete_node(ListNode(99))
    _assert_eq(head.to_list(), [1, 2, 3], "delete missing node")

    print("\nAll linked_list tests passed.")
