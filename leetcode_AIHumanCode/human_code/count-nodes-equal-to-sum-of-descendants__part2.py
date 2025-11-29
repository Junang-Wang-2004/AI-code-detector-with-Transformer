# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def equalToDescendants(self, root):
        """
        """
        def dfs(node, result):
            if not node:
                return 0
            total = dfs(node.left, result) + dfs(node.right, result)
            if node.val == total:
                result[0] += 1
            return total+node.val

        result = [0]
        dfs(root, result)
        return result[0]
