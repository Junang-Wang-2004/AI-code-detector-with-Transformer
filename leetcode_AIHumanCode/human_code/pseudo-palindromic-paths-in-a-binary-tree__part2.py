# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def pseudoPalindromicPaths (self, root):
        """
        """
        def dfs(node, count):
            if not root:
                return 0
            count ^= 1 << (node.val-1)
            return int(node.left == node.right and count&(count-1) == 0) + \
                   dfs(node.left, count) + dfs(node.right, count)
        return dfs(root, 0)
