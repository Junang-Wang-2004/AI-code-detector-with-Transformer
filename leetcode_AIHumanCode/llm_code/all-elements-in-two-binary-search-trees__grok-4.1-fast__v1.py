# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        def collect(node, vals):
            if node:
                collect(node.left, vals)
                vals.append(node.val)
                collect(node.right, vals)
        
        vals1, vals2 = [], []
        collect(root1, vals1)
        collect(root2, vals2)
        
        merged = []
        i, j = 0, 0
        while i < len(vals1) and j < len(vals2):
            if vals1[i] <= vals2[j]:
                merged.append(vals1[i])
                i += 1
            else:
                merged.append(vals2[j])
                j += 1
        merged.extend(vals1[i:])
        merged.extend(vals2[j:])
        return merged
