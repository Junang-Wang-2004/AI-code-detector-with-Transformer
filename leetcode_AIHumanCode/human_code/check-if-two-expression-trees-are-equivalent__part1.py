# Time:  O(n)
# Space: O(1)

import collections
import functools


# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        pass


# morris traversal
class Solution(object):
    def checkEquivalence(self, root1, root2):
        """
        """
        def add_counter(counter, prev, d, val):
            if val.isalpha():
                counter[ord(val)-ord('a')] += d if prev[0] == '+' else -d
            prev[0] = val
    
        def morris_inorder_traversal(root, cb):
            curr = root
            while curr:
                if curr.left is None:
                    cb(curr.val)
                    curr = curr.right
                else:
                    node = curr.left
                    while node.right and node.right != curr:
                        node = node.right
                    if node.right is None:
                        node.right = curr
                        curr = curr.left
                    else:
                        cb(curr.val)
                        node.right = None
                        curr = curr.right

        counter = collections.defaultdict(int)
        morris_inorder_traversal(root1, functools.partial(add_counter, counter, ['+'], 1))
        morris_inorder_traversal(root2, functools.partial(add_counter, counter, ['+'], -1))
        return all(v == 0 for v in counter.values())


