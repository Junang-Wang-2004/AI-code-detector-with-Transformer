class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        s1, s2 = [root], []
        while s1:
            nd = s1.pop()
            s2.append(nd)
            if nd.right:
                s1.append(nd.right)
            if nd.left:
                s1.append(nd.left)
        ans = []
        while s2:
            ans.append(s2.pop().val)
        return ans
