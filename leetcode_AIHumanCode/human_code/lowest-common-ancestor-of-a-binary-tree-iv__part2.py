# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        """
        def dfs(node, lookup):
            if not node or node in lookup:
                return node
            left, right = dfs(node.left, lookup), dfs(node.right, lookup)
            if left and right:
                return node
            return left or right
        
        return dfs(root, set(nodes))
