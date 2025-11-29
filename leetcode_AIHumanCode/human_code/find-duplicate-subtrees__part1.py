# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        """
        def getid(root, lookup, trees):
            if not root:
                return -1
            node_id = lookup[root.val,
                             getid(root.left, lookup, trees),
                             getid(root.right, lookup, trees)]
            trees[node_id].append(root)
            return node_id

        trees = collections.defaultdict(list)
        lookup = collections.defaultdict()
        lookup.default_factory = lookup.__len__
        getid(root, lookup, trees)
        return [roots[0] for roots in trees.values() if len(roots) > 1]


