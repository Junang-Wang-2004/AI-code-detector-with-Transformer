class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root, distance):
        self.res = 0
        def process(node):
            if node is None:
                return {}
            if node.left is None and node.right is None:
                return {0: 1}
            lmap = process(node.left)
            rmap = process(node.right)
            for dl in lmap:
                for dr in rmap:
                    if dl + dr + 2 <= distance:
                        self.res += lmap[dl] * rmap[dr]
            cmap = {}
            for d, c in lmap.items():
                cmap[d + 1] = cmap.get(d + 1, 0) + c
            for d, c in rmap.items():
                cmap[d + 1] = cmap.get(d + 1, 0) + c
            return cmap
        process(root)
        return self.res
