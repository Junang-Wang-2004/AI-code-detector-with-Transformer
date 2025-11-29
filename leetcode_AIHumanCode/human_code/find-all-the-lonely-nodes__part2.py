# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def getLonelyNodes(self, root):
        """
        """
        def dfs(node, result):
            if not node:
                return
            if node.left and not node.right:
                result.append(node.left.val)
            elif node.right and not node.left:
                result.append(node.right.val)
            dfs(node.left, result)
            dfs(node.right, result)

        result = []
        dfs(root, result)
        return result
