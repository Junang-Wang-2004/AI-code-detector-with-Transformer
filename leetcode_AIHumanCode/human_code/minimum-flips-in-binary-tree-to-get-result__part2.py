# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


import collections


# tree dp with stack
class Solution2(object):
    def minimumFlips(self, root, result):
        """
        """
        INF = float("inf")
        OP = {
            2: lambda x, y: x or y,
            3: lambda x, y: x and y,
            4: lambda x, y: x^y ,
            5: lambda x, y: not x if x is not None else not y
        }
        
        def dfs(node):
            if not node:
                return {None: 0}  # null object pattern
            if node.left == node.right:
                return {True: node.val^1, False: node.val^0}
            left = dfs(node.left)
            right = dfs(node.right)
            dp = collections.defaultdict(lambda: INF)
            for k1, v1 in left.items():
                for k2, v2 in right.items():
                    dp[OP[node.val](k1, k2)] = min(dp[OP[node.val](k1, k2)], v1+v2)
            return dp

        return dfs(root)[result]
