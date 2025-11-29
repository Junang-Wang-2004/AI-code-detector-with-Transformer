class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        stk = []
        curr = root
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans
