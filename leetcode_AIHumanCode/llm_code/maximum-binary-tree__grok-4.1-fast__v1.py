class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        stk = []
        for i in range(len(nums) - 1, -1, -1):
            curr = TreeNode(nums[i])
            while stk and nums[i] > stk[-1].val:
                curr.right = stk.pop()
            if stk:
                stk[-1].left = curr
            stk.append(curr)
        return stk[0]
