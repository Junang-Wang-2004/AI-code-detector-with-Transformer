# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def largestValues(self, root):
        """
        """
        result = []
        curr = [root]
        while any(curr):
            result.append(max(node.val for node in curr))
            curr = [child for node in curr for child in (node.left, node.right) if child]
        return result


