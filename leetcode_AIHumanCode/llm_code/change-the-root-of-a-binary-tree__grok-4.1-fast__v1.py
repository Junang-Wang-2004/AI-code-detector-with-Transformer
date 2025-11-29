# Definition for a Node.
class Node:
    def __init__(self, val):
        pass


class Solution(object):
    def flipBinaryTree(self, root, leaf):
        below = None
        cur = leaf
        while cur != root:
            above = cur.parent
            cur.parent = below
            if cur.left == below:
                cur.left = None
            elif cur.right == below:
                cur.right = None
            if cur.left:
                cur.right = cur.left
            cur.left = above
            below = cur
            cur = above
        root.parent = below
        if root.left == below:
            root.left = None
        elif root.right == below:
            root.right = None
        return leaf
