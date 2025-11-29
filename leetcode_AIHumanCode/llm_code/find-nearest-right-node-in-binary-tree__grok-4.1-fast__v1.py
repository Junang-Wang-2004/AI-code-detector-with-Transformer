class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findNeartestRightNode(self, root, u):
        if not root:
            return None
        que = [root]
        while que:
            sz = len(que)
            remaining = sz
            for _ in range(sz):
                curr = que.pop(0)
                remaining -= 1
                if curr == u:
                    return que[0] if remaining > 0 else None
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
        return None
