class Solution(object):
    def isValidSequence(self, root, arr):
        def go(curr, idx):
            if idx == len(arr) or not curr or curr.val != arr[idx]:
                return False
            if idx == len(arr) - 1:
                return curr.left is None and curr.right is None
            return go(curr.left, idx + 1) or go(curr.right, idx + 1)
        return go(root, 0)
