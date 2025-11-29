# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def diameterOfBinaryTree(self, root):
        """
        """
        def dfs(root):
            if not root: 
                return 0, 0
            left_d, left_h = dfs(root.left)
            right_d, right_h = dfs(root.right)
            return max(left_d, right_d, left_h+right_h), 1+max(left_h, right_h)
 
        return dfs(root)[0]
