class Solution(object):
    def minimumFuelCost(self, roads, seats):
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        fuel = [0]

        def traverse(curr, prev):
            passengers = 1
            for next_node in graph[curr]:
                if next_node != prev:
                    child_pass = traverse(next_node, curr)
                    fuel[0] += (child_pass + seats - 1) // seats
                    passengers += child_pass
            return passengers

        traverse(0, -1)
        return fuel[0]
