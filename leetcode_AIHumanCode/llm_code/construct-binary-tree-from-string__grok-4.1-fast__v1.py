class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution(object):
    def str2tree(self, s):
        if not s:
            return None
        idx = 0
        def build():
            nonlocal idx
            sign = -1 if s[idx] == '-' else 1
            if sign == -1:
                idx += 1
            num = 0
            while idx < len(s) and s[idx].isdigit():
                num = num * 10 + int(s[idx])
                idx += 1
            root = TreeNode(sign * num)
            if idx < len(s) and s[idx] == '(':
                idx += 1
                root.left = build()
                idx += 1
            if idx < len(s) and s[idx] == '(':
                idx += 1
                root.right = build()
                idx += 1
            return root
        return build()
