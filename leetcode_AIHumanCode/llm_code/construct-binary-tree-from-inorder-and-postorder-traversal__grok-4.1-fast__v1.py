class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        pos = {val: idx for idx, val in enumerate(inorder)}
        def construct(inL, inR, postL, postR):
            if inL > inR or postL > postR:
                return None
            rootVal = postorder[postR]
            root = TreeNode(rootVal)
            rootIdx = pos[rootVal]
            leftLen = rootIdx - inL
            root.left = construct(inL, rootIdx - 1, postL, postL + leftLen - 1)
            root.right = construct(rootIdx + 1, inR, postL + leftLen, postR - 1)
            return root
        return construct(0, len(inorder) - 1, 0, len(postorder) - 1)
