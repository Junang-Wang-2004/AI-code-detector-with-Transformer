# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def goodNodes(self, root):
        """
        """
        def dfs(node, curr_max):
            if not node:
                return 0
            curr_max = max(curr_max, node.val)
            return (int(curr_max <= node.val) +
                    dfs(node.left, curr_max) + dfs(node.right, curr_max))
        
        return dfs(root, root.val)
