class Solution(object):
    def splitBST(self, root, V):
        def traverse(curr):
            if curr is None:
                return [None, None]
            if curr.val <= V:
                sub = traverse(curr.right)
                curr.right = sub[0]
                return [curr, sub[1]]
            sub = traverse(curr.left)
            curr.left = sub[1]
            return [sub[0], curr]
        res = traverse(root)
        return res[0], res[1]
