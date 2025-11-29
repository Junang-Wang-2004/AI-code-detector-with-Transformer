# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def diameter(self, root):
        """
        """
        def dfs(node):
            max_dia, max_depth = 0, 0
            for child in node.children:
                child_max_dia, child_max_depth = dfs(child)
                max_dia = max(max_dia, child_max_dia, max_depth+child_max_depth+1)
                max_depth = max(max_depth, child_max_depth+1)
            return max_dia, max_depth
        
        return dfs(root)[0]
