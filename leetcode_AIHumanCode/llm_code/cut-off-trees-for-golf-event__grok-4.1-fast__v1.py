import heapq

class Solution:
    def cutOffTree(self, forest):
        if not forest:
            return 0
        rows, cols = len(forest), len(forest[0])
        trees = []
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()

        def shortest_distance(fr, fc, tr, tc):
            if fr == tr and fc == tc:
                return 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            pq = []
            heapq.heappush(pq, (abs(fr - tr) + abs(fc - tc), 0, fr, fc))
            seen = set()
            while pq:
                est, steps, r, c = heapq.heappop(pq)
                pos = (r, c)
                if pos in seen:
                    continue
                seen.add(pos)
                if r == tr and c == tc:
                    return steps
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and forest[nr][nc] > 0:
                        npos = (nr, nc)
                        if npos not in seen:
                            nh = abs(nr - tr) + abs(nc - tc)
                            nf = steps + 1 + nh
                            heapq.heappush(pq, (nf, steps + 1, nr, nc))
            return -1

        cr, cc = 0, 0
        total = 0
        for _, tr, tc in trees:
            steps = shortest_distance(cr, cc, tr, tc)
            if steps == -1:
                return -1
            total += steps
            cr, cc = tr, tc
        return total
