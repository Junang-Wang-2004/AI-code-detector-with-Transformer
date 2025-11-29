class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        def construct(low, high):
            if low >= high:
                return None
            pivot = low + (high - low) // 2
            root = TreeNode(nums[pivot])
            root.left = construct(low, pivot)
            root.right = construct(pivot + 1, high)
            return root
        return construct(0, len(nums))
