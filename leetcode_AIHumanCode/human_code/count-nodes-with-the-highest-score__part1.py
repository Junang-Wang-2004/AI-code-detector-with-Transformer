from functools import reduce
# Time:  O(n)
# Space: O(n)

class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        """
        def iter_dfs(adj):
            result = [0]*2
            stk = [(1, (0, [0]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    i, ret = args
                    cnts = [[0] for _ in range(len(adj[i]))]
                    stk.append((2, (cnts, ret)))
                    for j, child in enumerate(adj[i]):
                        stk.append((1, (child, cnts[j])))
                elif step == 2:
                    cnts, ret = args
                    ret[0] = sum(cnt[0] for cnt in cnts)+1
                    score = max((len(adj)-ret[0]), 1)*reduce(lambda x, y: x*y[0], cnts, 1)
                    if score > result[0]:
                        result[:] = [score, 1]
                    elif score == result[0]:
                        result[1] += 1
            return result[1]

        adj = [[] for _ in range(len(parents))]  # Space: O(n)
        for i in range(1, len(parents)):
            adj[parents[i]].append(i)
        return iter_dfs(adj)


