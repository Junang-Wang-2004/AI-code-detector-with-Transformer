# Time:  O(n)
# Space: O(h)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def diameter(self, root):
        """
        """
        def iter_dfs(root):
            result = [0]*2
            stk = [(1, (root, result))]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, ret = params
                    for child in reversed(node.children):
                        ret2 = [0]*2
                        stk.append((2, (ret2, ret)))
                        stk.append((1, (child, ret2)))
                else:
                    ret2, ret = params
                    ret[0] = max(ret[0], ret2[0], ret[1]+ret2[1]+1)
                    ret[1] = max(ret[1], ret2[1]+1)
            return result
        
        return iter_dfs(root)[0]


