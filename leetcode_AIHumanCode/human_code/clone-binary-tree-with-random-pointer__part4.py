# Time:  O(n)
# Space: O(n)
import collections


class Solution2_Recu(object):
    def copyRandomBinaryTree(self, root):
        """
        """ 
        def dfs(node, lookup):
            if not node:
                return
            lookup[node].val = node.val
            lookup[node].left = lookup[node.left]
            lookup[node].right = lookup[node.right]
            lookup[node].random = lookup[node.random]
            dfs(node.left, lookup)
            dfs(node.right, lookup)
    
        lookup = collections.defaultdict(lambda: NodeCopy())
        lookup[None] = None
        dfs(root, lookup)
        return lookup[root]
