# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)                
            result.append(node.val)
            current = next_level

        return result

