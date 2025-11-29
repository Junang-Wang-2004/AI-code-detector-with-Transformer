# Time:  O(n)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        pass


class Solution2(object):
    def findRoot(self, tree):
        """
        """
        root = 0
        for node in tree:
            root ^= node.val
            for child in node.children:
                root ^= child.val
        for node in tree:
            if node.val == root:
                return node
        return None


