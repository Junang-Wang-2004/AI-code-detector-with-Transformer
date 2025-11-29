# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        """        
        def dfs(node, p, q, result):
            if not node:
                return 0
            left = dfs(node.left, p, q, result)
            right = dfs(node.right, p, q, result)
            curr = int(node == p or node == q)
            if curr+left+right == 2 and not result[0]:
                result[0] = node
            return curr+left+right

        result = [0]
        dfs(root, p, q, result)
        return result[0]

