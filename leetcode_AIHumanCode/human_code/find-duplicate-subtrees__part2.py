# Time:  O(n * h)
# Space: O(n * h)
class Solution2(object):
    def findDuplicateSubtrees(self, root):
        """
        """
        def postOrderTraversal(node, lookup, result):
            if not node:
                return ""
            s = "(" + postOrderTraversal(node.left, lookup, result) + \
                str(node.val) + \
                postOrderTraversal(node.right, lookup, result) + \
                ")"
            if lookup[s] == 1:
                result.append(node)
            lookup[s] += 1
            return s

        lookup = collections.defaultdict(int)
        result = []
        postOrderTraversal(root, lookup, result)
        return result

