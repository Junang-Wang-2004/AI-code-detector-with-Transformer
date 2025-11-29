# Time:  O(n)
# Space: O(h)
import collections
import functools


class Solution2(object):
    def checkEquivalence(self, root1, root2):
        """
        """
        def add_counter(counter, prev, d, val):
            if val.isalpha():
                counter[ord(val)-ord('a')] += d if prev[0] == '+' else -d
            prev[0] = val

        def inorder_traversal(root, cb):
            def traverseLeft(node, stk):
                while node:
                    stk.append(node)
                    node = node.left 

            stk = []
            traverseLeft(root, stk)
            while stk:
                curr = stk.pop()
                cb(curr.val)
                traverseLeft(curr.right, stk)
                
        counter = collections.defaultdict(int)
        inorder_traversal(root1, functools.partial(add_counter, counter, ['+'], 1))
        inorder_traversal(root2, functools.partial(add_counter, counter, ['+'], -1))
        return all(v == 0 for v in counter.values())
