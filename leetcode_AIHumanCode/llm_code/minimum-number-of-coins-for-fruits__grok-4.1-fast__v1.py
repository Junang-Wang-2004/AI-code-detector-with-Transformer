import collections

class Solution(object):
    def minimumCoins(self, prices):
        n = len(prices)
        INF = 10**18 + 5
        vals = [INF] * (n + 1)
        vals[0] = 0
        que = collections.deque()
        for idx in range(n):
            cval = vals[idx] + prices[idx]
            while que and vals[que[-1]] + prices[que[-1]] >= cval:
                que.pop()
            que.append(idx)
            lft = idx // 2
            while que and que[0] < lft:
                que.popleft()
            vals[idx + 1] = vals[que[0]] + prices[que[0]]
        return vals[-1]
