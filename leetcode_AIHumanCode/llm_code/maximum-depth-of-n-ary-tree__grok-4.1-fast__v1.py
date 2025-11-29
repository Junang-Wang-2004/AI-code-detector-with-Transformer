class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        maximum = 0
        pile = []
        if root:
            pile.append((root, 1))
        while pile:
            present, level = pile.pop()
            if level > maximum:
                maximum = level
            for next_node in present.children:
                pile.append((next_node, level + 1))
        return maximum
