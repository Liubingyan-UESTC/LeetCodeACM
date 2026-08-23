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

    def print_tree(self):
        if not self:
            print("(empty)")
            return

        # 计算树的高度
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        h = get_height(self)
        # 画布宽度 = 2^(h+1) + 1，让根节点居中并留出足够空间放左右子树
        width = 2 ** (h + 1) + 1
        grid = [[' '] * width for _ in range(2 * h + 1)]

        def place(node, depth, col, span):
            if node is None:
                return
            val_str = str(node.val)
            for i, ch in enumerate(val_str):
                grid[depth * 2][col + i] = ch
            if node.left:
                grid[depth * 2 + 1][col - 1] = '/'
                place(node.left, depth + 1, col - span, span)
            if node.right:
                grid[depth * 2 + 1][col + 1] = '\\'
                place(node.right, depth + 1, col + span, span)

        place(self, 0, width // 2, 2)

        for row in grid:
            print(''.join(row).rstrip())

        
