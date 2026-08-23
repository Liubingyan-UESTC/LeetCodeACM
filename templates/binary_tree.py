from collections import deque

class TreeNode:
    def __init__(self , 
                 val = 0 , 
                 left:"TreeNode|None" = None , 
                 right : "TreeNode|None" = None):
        self.val = val
        self.left = left 
        self.right = right

    def get_left(self) -> 'TreeNode | None':
        return self.left

    def get_right(self) -> 'TreeNode | None':
        return self.right

    def build_tree(self , node_list):
        if not node_list or node_list[0] is None:
            return None
        root = TreeNode(node_list[0])
        queue = deque([root])
        i = 1
        while queue and i < len(node_list):
            node = queue.popleft()
            if i < len(node_list):
                if node_list[i] is not None:
                    node.left = TreeNode(node_list[i])
                    queue.append(node.left)
                i += 1
            if i < len(node_list):
                if node_list[i] is not None:
                    node.right = TreeNode(node_list[i])
                    queue.append(node.right)
                i += 1
        return root
        
