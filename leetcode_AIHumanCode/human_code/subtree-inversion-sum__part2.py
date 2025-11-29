# Time:  O(n)
# Space: O(n)
# dfs, tree dp
class Solution2(object):
    def subtreeInversionSum(self, edges, nums, k):
        """
        """
        def dfs(u, p):
            dp.append([0]*2)
            total, pos, neg = nums[u], 0, 0
            for v in adj[u]:
                if v == p:
                    continue
                new_total, new_pos, new_neg = dfs(v, u)
                total += new_total
                pos += new_pos
                neg += new_neg
            pos = max(pos, dp[-1][1]-2*total)
            neg = max(neg, dp[-1][0]+2*total)
            dp.pop()
            if len(dp)-k >= 0:
                dp[len(dp)-k][0] += pos
                dp[len(dp)-k][1] += neg
            return total, pos, neg

        adj = [[] for _ in range(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = []
        total, pos, neg = dfs(0, -1)
        return total+pos
