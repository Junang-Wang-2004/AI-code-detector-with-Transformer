import collections
import heapq

class GridMaster(object):
    def canMove(self, direction):
        pass

    def move(self, direction):
        pass

    def isTarget(self):
        pass

class Solution(object):
    def findShortestPath(self, master):
        dir_delta = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        opp_delta = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

        def explore(curr, goal_ref, gm, seen, edges):
            if goal_ref[0] is None and gm.isTarget():
                goal_ref[0] = curr
            seen.add(curr)
            for dname, (di, dj) in dir_delta.items():
                if not gm.canMove(dname):
                    continue
                nxt = (curr[0] + di, curr[1] + dj)
                if nxt in edges[curr]:
                    continue
                fwd_cost = gm.move(dname)
                edges[curr][nxt] = fwd_cost
                if nxt not in seen:
                    explore(nxt, goal_ref, gm, seen, edges)
                back_cost = gm.move(opp_delta[dname])
                edges[nxt][curr] = back_cost

        def min_distance(g, source, dest):
            costs = {source: 0}
            pq = [(0, source)]
            while pq:
                weight, vertex = heapq.heappop(pq)
                if weight > costs.get(vertex, float('inf')):
                    continue
                for adj_node, edge_wt in g[vertex].items():
                    candidate = weight + edge_wt
                    if candidate < costs.get(adj_node, float('inf')):
                        costs[adj_node] = candidate
                        heapq.heappush(pq, (candidate, adj_node))
            return costs.get(dest, -1)

        init_pos = (0, 0)
        goal_ref = [None]
        edge_map = collections.defaultdict(dict)
        seen_pos = set()
        explore(init_pos, goal_ref, master, seen_pos, edge_map)
        if goal_ref[0] is None:
            return -1
        return min_distance(edge_map, init_pos, goal_ref[0])
