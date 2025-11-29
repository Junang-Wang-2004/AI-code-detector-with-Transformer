import collections
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: TreeNode, queries: List[int]) -> List[int]:
        deps = {}
        hts = {}
        max_h1 = collections.defaultdict(int)
        max_h2 = collections.defaultdict(int)

        def measure(node, level):
            if not node:
                return 0
            lmax = measure(node.left, level + 1)
            rmax = measure(node.right, level + 1)
            subtree_h = 1 + max(lmax, rmax)
            deps[node.val] = level
            hts[node.val] = subtree_h
            if subtree_h > max_h1[level]:
                max_h2[level] = max_h1[level]
                max_h1[level] = subtree_h
            elif subtree_h > max_h2[level]:
                max_h2[level] = subtree_h
            return subtree_h

        if root:
            measure(root, 0)

        result = []
        for node_val in queries:
            lv = deps[node_val]
            nh = hts[node_val]
            alt_h = max_h2[lv] if nh == max_h1[lv] else max_h1[lv]
            result.append(lv - 1 + alt_h)
        return result
