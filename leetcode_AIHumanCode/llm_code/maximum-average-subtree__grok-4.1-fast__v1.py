class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        self.max_avg = 0.0

        def traverse(curr):
            if not curr:
                return 0, 0
            lsum, lsize = traverse(curr.left)
            rsum, rsize = traverse(curr.right)
            totalsum = lsum + rsum + curr.val
            totalsize = lsize + rsize + 1
            self.max_avg = max(self.max_avg, totalsum / totalsize)
            return totalsum, totalsize

        traverse(root)
        return self.max_avg
