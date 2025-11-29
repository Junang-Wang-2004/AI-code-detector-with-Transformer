# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        flips = []
        
        def traverse(node, pos):
            if node is None:
                return pos, True
            if pos >= len(voyage) or node.val != voyage[pos]:
                return -1, False
            pos += 1
            flipped = False
            if node.left is not None:
                next_pos = pos
                if next_pos < len(voyage) and node.left.val == voyage[next_pos]:
                    pos, ok = traverse(node.left, pos)
                    if not ok:
                        return -1, False
                else:
                    if node.right is None:
                        return -1, False
                    flips.append(node.val)
                    flipped = True
                    pos, ok = traverse(node.right, pos)
                    if not ok:
                        return -1, False
                    pos, ok = traverse(node.left, pos)
                    if not ok:
                        return -1, False
            if not flipped and node.right is not None:
                pos, ok = traverse(node.right, pos)
                if not ok:
                    return -1, False
            return pos, True
        
        end_pos, matched = traverse(root, 0)
        if matched and end_pos == len(voyage):
            return flips
        return [-1]
