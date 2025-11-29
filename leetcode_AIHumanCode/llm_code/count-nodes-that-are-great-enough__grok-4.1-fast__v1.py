import heapq
from itertools import islice

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countGreatEnoughNodes(self, root, k):
        def traverse(curr):
            if not curr:
                return []
            l_vals = traverse(curr.left)
            r_vals = traverse(curr.right)
            sub_vals = list(islice(heapq.merge(l_vals, r_vals), k))
            if len(sub_vals) == k and (k == 0 or sub_vals[-1] < curr.val):
                self.counter += 1
            combined = list(islice(heapq.merge(sub_vals, [curr.val]), k))
            return combined

        self.counter = 0
        traverse(root)
        return self.counter
