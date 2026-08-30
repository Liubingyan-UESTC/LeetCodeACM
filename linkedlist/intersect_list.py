from templates.linked_list import ListNode

def intersect_list_node(head1 : ListNode , head2: ListNode):
    p1 = head1
    p2 = head2
    while p1 != p2:
        p1 = p1.next if p1 else head2
        p2 = p2.next if p2 else head1
    return p1

def main():
    common_node1 = ListNode(100 , None)
    common_node2 = ListNode(102 , common_node1)
    common_node3 = ListNode(103 , common_node2)

    head1 = ListNode().create([1,2,3,4,5,6,7] ,head_insert = False)
    head2 = ListNode().create([8,9,10,11,12] , head_insert= False)
    p = head1
    q = head2
    while p.next:
        p = p.next
    while q.next:
        q = q.next
    p.next = common_node3
    q.next = common_node3

    print(intersect_list_node(head1 , head2).val)

main()

