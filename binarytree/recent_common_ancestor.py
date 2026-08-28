# 二叉树的最近公共祖先
import sys
from templates.binary_tree import TreeNode

def find_recent_common_ancestor(
        root : TreeNode , 
        node1 : TreeNode , 
        node2 : TreeNode):

    if not root or root == node1 or root == node2:
        return root

    left = find_recent_common_ancestor(root.left,node1,node2)
    right = find_recent_common_ancestor(root.right , node1 , node2)

    if left and right:
        return root
    else:
        return left if left else right

def main():
    # root = TreeNode().build_tree([1,2,3,4,None , None, 5,None , 6,7,None])
    # root.print_tree()
    # print()
    node_1 = TreeNode(0)
    node_2 = TreeNode(1)
    node_3 = TreeNode(2)
    node_4 = TreeNode(3)
    node_5 = TreeNode(4 , node_3 , node_4)
    node_6 = TreeNode(5 , None , node_5)
    node_7 = TreeNode(6 , node_2 , node_1)
    root = TreeNode(100 , node_7 , node_6)

    root.print_tree()
    print(find_recent_common_ancestor(root , node_1 , node_4).val)
if __name__ == "__main__":
    main()
    