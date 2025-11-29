# Time:  O(t * (logt + m * n)), t is the number of trees
# Space: O(t + m * n)
class Solution_TLE(object):
    def cutOffTree(self, forest):
        """
        """
        def minStep(p1, p2):
            min_steps = 0
            lookup = {p1}
            q = collections.deque([p1])
            while q:
                size = len(q)
                for _ in range(size):
                    (i, j) = q.popleft()
                    if (i, j) == p2:
                        return min_steps
                    for i, j in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                        if not (0 <= i < m and 0 <= j < n and forest[i][j] and (i, j) not in lookup):
                            continue
                        q.append((i, j))
                        lookup.add((i, j))
                min_steps += 1
            return -1

        m, n = len(forest), len(forest[0])
        min_heap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(min_heap, (forest[i][j], (i, j)))

        start = (0, 0)
        result = 0
        while min_heap:
            tree = heapq.heappop(min_heap)
            step = minStep(start, tree[1])
            if step < 0:
                return -1
            result += step
            start = tree[1]
        return result

