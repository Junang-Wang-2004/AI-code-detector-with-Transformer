from functools import reduce
# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def countHighestScoreNodes(self, parents):
        """
        """
        def dfs(adj, i, result):
            cnts = [dfs(adj, child, result) for child in adj[i]]
            total = sum(cnts)+1
            score = max((len(adj)-total), 1)*reduce(lambda x, y: x*y, cnts, 1)
            if score > result[0]:
                result[:] = [score, 1]
            elif score == result[0]:
                result[1] += 1
            return total

        adj = [[] for _ in range(len(parents))]  # Space: O(n)
        for i in range(1, len(parents)):
            adj[parents[i]].append(i)
        result = [0]*2
        dfs(adj, 0, result)
        return result[1]
