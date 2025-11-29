# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# dfs
class Solution(object):
    def heightOfTree(self, root):
        """
        """
        result = -1
        stk = [(root, 0)]
        while stk:
            u, d = stk.pop()
            result = max(result, d)
            if u.right and u.right.left != u:
                stk.append((u.right, d+1))
            if u.left and u.left.right != u:
                stk.append((u.left, d+1))
        return result


