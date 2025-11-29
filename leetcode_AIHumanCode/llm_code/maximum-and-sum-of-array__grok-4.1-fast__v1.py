class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        N = 2 * numSlots
        nums += [0] * (N - len(nums))
        V = 2 * N + 2
        s = 2 * N
        t = 2 * N + 1
        INF = 10**18
        graph = [[] for _ in range(V)]

        def add_edge(fr, to, cap, cost):
            graph[fr].append([to, cap, cost, len(graph[to])])
            graph[to].append([fr, 0, -cost, len(graph[fr]) - 1])

        for i in range(N):
            add_edge(s, i, 1, 0)
        for j in range(N):
            add_edge(N + j, t, 1, 0)
        for i in range(N):
            for j in range(N):
                slot_val = 1 + (j // 2)
                cost = -(nums[i] & slot_val)
                add_edge(i, N + j, 1, cost)

        h = [0] * V
        dist = [0] * V
        prevv = [0] * V
        preve = [0] * V
        import heapq
        res = 0
        f = N
        while f > 0:
            dist[:] = [INF] * V
            dist[s] = 0
            q = [(0, s)]
            while q:
                p = heapq.heappop(q)
                dd, v = p[0], p[1]
                if dd > dist[v]:
                    continue
                for i in range(len(graph[v])):
                    edge = graph[v][i]
                    if edge[1] > 0:
                        to = edge[0]
                        reduced_cost = edge[2] + h[v] - h[to]
                        if dist[to] > dist[v] + reduced_cost:
                            newd = dist[v] + reduced_cost
                            dist[to] = newd
                            prevv[to] = v
                            preve[to] = i
                            heapq.heappush(q, (newd, to))
            if dist[t] == INF:
                break
            for v in range(V):
                if dist[v] < INF:
                    h[v] += dist[v]
            d = f
            v = t
            while v != s:
                d = min(d, graph[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * h[t]
            v = t
            while v != s:
                e = graph[prevv[v]][preve[v]]
                e[1] -= d
                rev_e = graph[v][e[3]]
                rev_e[1] += d
                v = prevv[v]
        return -res
