# Time:  O(n)
# Space: O(n)
import collections


class Solution2(object):
    def copyRandomBinaryTree(self, root):
        """
        """ 
        lookup = collections.defaultdict(lambda: NodeCopy())
        lookup[None] = None
        stk = [root]
        while stk:
            node = stk.pop()
            if not node:
                continue
            lookup[node].val = node.val
            lookup[node].left = lookup[node.left]
            lookup[node].right = lookup[node.right]
            lookup[node].random = lookup[node.random]
            stk.append(node.right)
            stk.append(node.left)
        return lookup[root]


