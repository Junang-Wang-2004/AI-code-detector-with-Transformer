# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def cloneTree(self, root):
        """
        """
        def dfs(node):
            if not node:
                return None
            copy = Node(node.val)
            for child in node.children:
                copy.children.append(dfs(child))
            return copy
        
        return dfs(root)
