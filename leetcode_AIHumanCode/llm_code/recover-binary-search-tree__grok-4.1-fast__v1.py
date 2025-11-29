class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):
        stack = []
        curr = root
        prev = None
        fst = None
        snd = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and prev.val > curr.val:
                if fst is None:
                    fst = prev
                snd = curr
            prev = curr
            curr = curr.right
        if fst:
            fst.val, snd.val = snd.val, fst.val
        return root
