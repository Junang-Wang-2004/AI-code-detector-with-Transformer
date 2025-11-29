# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def findDistance(self, root, p, q):
        """
        """
        def dfs(node, p, q, result):
            if not node:
                return -1
            left = dfs(node.left, p, q, result)
            right = dfs(node.right, p, q, result)
            if node.val in (p, q):
                if left == right == -1:
                    return 0
                result[0] = left+1 if left != -1 else right+1
            if left != -1 and right != -1:
                result[0] = left+right+2
            elif left != -1:
                return left+1
            elif right != -1:
                return right+1
            return -1
        
        result = [0]
        dfs(root, p, q, result)
        return result[0]
