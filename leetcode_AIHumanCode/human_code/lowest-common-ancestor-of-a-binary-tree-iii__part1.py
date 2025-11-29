# Time:  O(h)
# Space: O(1)

# Definition for a Node.
class Node:
    def __init__(self, val):
        pass

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        """
        a, b = p, q
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a


