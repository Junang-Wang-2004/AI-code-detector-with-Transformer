# Time:  O(n + qlogn)
# Space: O(n)
import bisect


# dfs, binary search
class Solution2(object):
    def closestNodes(self, root, queries):
        """
        """
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        inorder = []
        dfs(root)
        result = []
        for q in queries:
            i = bisect.bisect_left(inorder, q)
            if i == len(inorder):
                result.append([inorder[i-1], -1])
            elif inorder[i] == q:
                result.append([inorder[i], inorder[i]])
            elif i-1 >= 0:
                result.append([inorder[i-1], inorder[i]])
            else:
                result.append([-1, inorder[i]])
        return result
