class TreeNode:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def get_left(self) -> 'TreeNode | None':
        return self.left
    
    def get_right(self) -> 'TreeNode | None':
        return self.right
    
    
