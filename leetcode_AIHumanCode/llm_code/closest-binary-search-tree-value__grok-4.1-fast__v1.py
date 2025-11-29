class Solution:
    def closestValue(self, root, target):
        lower = None
        upper = None
        node = root
        while node:
            if node.val <= target:
                lower = node.val
                node = node.right
            else:
                node = node.left
        node = root
        while node:
            if node.val >= target:
                upper = node.val
                node = node.left
            else:
                node = node.right
        if lower is None:
            return upper
        if upper is None:
            return lower
        return lower if abs(lower - target) <= abs(upper - target) else upper
