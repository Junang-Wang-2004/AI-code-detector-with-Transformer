class Solution(object):
    def longestConsecutive(self, root):
        def dfs(node):
            if not node:
                return 0, 0
            left_down, left_mx = dfs(node.left)
            right_down, right_mx = dfs(node.right)
            down_len = 1
            if node.left and node.left.val == node.val + 1:
                down_len = max(down_len, left_down + 1)
            if node.right and node.right.val == node.val + 1:
                down_len = max(down_len, right_down + 1)
            sub_max = max(down_len, left_mx, right_mx)
            return down_len, sub_max

        if not root:
            return 0
        _, result = dfs(root)
        return result
