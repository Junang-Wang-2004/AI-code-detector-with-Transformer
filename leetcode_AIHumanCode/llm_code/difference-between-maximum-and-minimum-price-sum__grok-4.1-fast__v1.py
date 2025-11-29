class Solution(object):
    def maxOutput(self, n, edges, price):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        ans = max(price)
        INF = 10**18

        def explore(node, parent):
            nonlocal ans
            ans = max(ans, price[node])
            max1 = -INF
            max2 = -INF
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                ch_max = explore(nxt, node)
                ans = max(ans, price[node] + ch_max)
                ans = max(ans, price[node] + max1 + ch_max)
                ans = max(ans, price[node] + max2 + ch_max)
                if ch_max > max1:
                    max2 = max1
                    max1 = ch_max
                elif ch_max > max2:
                    max2 = ch_max
            ch_ext = max1 if max1 > -INF else -INF
            return price[node] + max(0, ch_ext)

        explore(0, -1)
        return ans
