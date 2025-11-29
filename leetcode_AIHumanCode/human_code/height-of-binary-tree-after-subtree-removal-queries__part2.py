# Time:  O(n)
# Space: O(n)
import collections


# dfs
class Solution2(object):
    def treeQueries(self, root, queries):
        """
        """
        def dfs(curr, d):
            if not curr:
                return 0
            h = 1+max(dfs(curr.left, d+1), dfs(curr.right, d+1))
            if h > top[d][0]:
                top[d][0], top[d][1] = h, top[d][0]
            elif h > top[d][1]:
                top[d][1] = h
            depth[curr.val], height[curr.val] = d, h
            return h
        
        top = collections.defaultdict(lambda: [0]*2)
        depth, height = {}, {}
        dfs(root, 0)
        return [(depth[q]-1)+(top[depth[q]][0] if height[q] != top[depth[q]][0] else top[depth[q]][1]) for q in queries]
