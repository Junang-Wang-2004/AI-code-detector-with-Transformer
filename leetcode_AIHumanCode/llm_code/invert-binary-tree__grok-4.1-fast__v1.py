class Solution:
    def invertTree(self, root):
        def dfs(curr):
            if curr:
                dfs(curr.left)
                dfs(curr.right)
                curr.left, curr.right = curr.right, curr.left
        dfs(root)
        return root
