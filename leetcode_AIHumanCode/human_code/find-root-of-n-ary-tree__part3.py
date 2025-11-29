# Time:  O(n)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        pass


class Solution3(object):
    def findRoot(self, tree):
        """
        """
        root = 0
        for node in tree:
            root += node.val-sum(child.val for child in node.children)
        for node in tree:
            if node.val == root:
                return node
        return None
