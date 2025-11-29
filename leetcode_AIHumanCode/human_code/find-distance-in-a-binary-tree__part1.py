# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


class Solution(object):
    def findDistance(self, root, p, q):
        """
        """
        def iter_dfs(root, p, q):
            result = 0
            dist = [-1]
            stk = [(1, [root, dist])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, ret = params
                    if not node:
                        continue
                    ret1, ret2 = [-1], [-1]
                    stk.append((2, [node, ret1, ret2, ret]))
                    stk.append((1, [node.right, ret2]))
                    stk.append((1, [node.left, ret1]))
                elif step == 2:
                    node, ret1, ret2, ret = params
                    if node.val in (p, q):
                        if ret1[0] == ret2[0] == -1:
                            ret[0] = 0
                        else:
                            result = ret1[0]+1 if ret1[0] != -1 else ret2[0]+1
                    elif ret1[0] != -1 and ret2[0] != -1:
                        result = ret1[0]+ret2[0]+2
                    elif ret1[0] != -1:
                        ret[0] = ret1[0]+1
                    elif ret2[0] != -1:
                        ret[0] = ret2[0]+1
            return result
        
        return iter_dfs(root, p, q)
                    

