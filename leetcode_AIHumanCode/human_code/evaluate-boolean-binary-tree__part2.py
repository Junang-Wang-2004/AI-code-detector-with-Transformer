# Time:  O(n)
# Space: O(h)
# dfs with recursion
class Solution2(object):
    def evaluateTree(self, root):
        """
        """
        INF = float("inf")
        OP = {
            2: lambda x, y: x or y,
            3: lambda x, y: x and y,
        }
        
        def dfs(node):
            if node.left == node.right:
                return node.val
            return OP[node.val](dfs(node.left), dfs(node.right))

        return dfs(root)
