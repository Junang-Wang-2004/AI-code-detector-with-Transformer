# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def canMerge(self, trees):
        attach_vals = set()
        root_dict = {}
        for tr in trees:
            root_dict[tr.val] = tr
            stack = [tr]
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None and node != tr:
                    attach_vals.add(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        main_root = None
        for tr in trees:
            if tr.val not in attach_vals:
                if main_root is not None:
                    return None
                main_root = tr
        if main_root is None:
            return None
        del root_dict[main_root.val]

        def validate_and_merge(curr, lo, hi):
            if not (lo < curr.val < hi):
                return False
            if curr.left:
                lval = curr.left.val
                if lval in attach_vals and lval in root_dict:
                    curr.left = root_dict[lval]
                    del root_dict[lval]
                if not validate_and_merge(curr.left, lo, curr.val):
                    return False
            if curr.right:
                rval = curr.right.val
                if rval in attach_vals and rval in root_dict:
                    curr.right = root_dict[rval]
                    del root_dict[rval]
                if not validate_and_merge(curr.right, curr.val, hi):
                    return False
            return True

        if validate_and_merge(main_root, float('-inf'), float('inf')) and not root_dict:
            return main_root
        return None
