# Time:  O(n)
# Space: O(h)
# dfs
class Solution2(object):
    def averageOfSubtree(self, root):
        """
        """
        def dfs(node):
            if not node:
                return [0]*3
            left = dfs(node.left)
            right = dfs(node.right)
            return [left[0]+right[0]+node.val,
                    left[1]+right[1]+1,
                    left[2]+right[2]+int((left[0]+right[0]+node.val)//(left[1]+right[1]+1) == node.val)]
        
        return dfs(root)[2]
