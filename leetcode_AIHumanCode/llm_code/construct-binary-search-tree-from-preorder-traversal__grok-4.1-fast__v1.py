class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        path = [root]
        for num in preorder[1:]:
            curr = TreeNode(num)
            if num < path[-1].val:
                path[-1].left = curr
            else:
                parent = None
                while path and path[-1].val < num:
                    parent = path.pop()
                parent.right = curr
            path.append(curr)
        return root
