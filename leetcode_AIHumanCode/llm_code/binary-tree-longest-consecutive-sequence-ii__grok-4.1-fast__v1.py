class Solution(object):
    def longestConsecutive(self, root):
        res = [0]
        def dfs(node):
            if not node:
                return 0, 0
            l_up, l_down = dfs(node.left)
            r_up, r_down = dfs(node.right)
            up = 1
            if node.left and node.left.val == node.val + 1:
                up = max(up, l_up + 1)
            if node.right and node.right.val == node.val + 1:
                up = max(up, r_up + 1)
            down = 1
            if node.left and node.left.val == node.val - 1:
                down = max(down, l_down + 1)
            if node.right and node.right.val == node.val - 1:
                down = max(down, r_down + 1)
            res[0] = max(res[0], up + down - 1)
            return up, down
        dfs(root)
        return res[0]
