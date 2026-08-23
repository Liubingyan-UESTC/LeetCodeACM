# 二叉树的最大深度
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from templates.binary_tree import TreeNode


input = sys.stdin.readline 

def get_depth(root : TreeNode|None):
    if not root:
        return 0
    return max(get_depth(root.left) + 1,get_depth(root.right) + 1) 


def main():
    nodes = [1,2,3,None , 5,7,8]
    root = TreeNode().build_tree(nodes)
    print(get_depth(root))

if __name__ == "__main__":
    main()