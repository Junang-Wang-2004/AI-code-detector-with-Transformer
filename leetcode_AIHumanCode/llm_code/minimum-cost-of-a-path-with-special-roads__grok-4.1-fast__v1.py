import collections
import heapq
from math import inf

class Solution:
    def minimumCost(self, source, destination, highways):
        src = tuple(source)
        dst = tuple(destination)
        specials = collections.defaultdict(list)
        specials[dst] = []
        for x0, y0, x1, y1, toll in highways:
            specials[(x0, y0)].append(((x1, y1), toll))
        candidates = list(specials.keys())
        distances = {}
        frontier = []
        heapq.heappush(frontier, (0, src))
        distances[src] = 0
        while frontier:
            distance, here = heapq.heappop(frontier)
            if distance > distances.get(here, inf):
                continue
            if here == dst:
                return distance
            for there, toll in specials[here]:
                candidate = distance + toll
                if candidate < distances.get(there, inf):
                    distances[there] = candidate
                    heapq.heappush(frontier, (candidate, there))
            for candidate_pos in candidates:
                move_cost = abs(here[0] - candidate_pos[0]) + abs(here[1] - candidate_pos[1])
                candidate = distance + move_cost
                if candidate < distances.get(candidate_pos, inf):
                    distances[candidate_pos] = candidate
                    heapq.heappush(frontier, (candidate, candidate_pos))
        return distances.get(dst, inf)
