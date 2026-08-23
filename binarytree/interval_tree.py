# 翻转二叉树
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from templates.binary_tree import TreeNode

input = sys.stdin.readline 

def interval_tree(root : TreeNode | None) -> TreeNode | None:
    if not root:
        return None
    root.left , root.right = root.right , root.left
    interval_tree(root.left)
    interval_tree(root.right)
    return root

def main():
    nodes = [1,2,3,None , 5,None , None , 7 , 8]
    root = TreeNode().build_tree(nodes)
    if root is not None:
        root.print_tree()
        print()
        flipped = interval_tree(root)
        if flipped is not None:
            flipped.print_tree()

if __name__ == "__main__":
    main()