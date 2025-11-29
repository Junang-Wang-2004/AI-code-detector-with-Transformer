class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        output = []
        
        def dfs(node):
            if node:
                output.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return output
