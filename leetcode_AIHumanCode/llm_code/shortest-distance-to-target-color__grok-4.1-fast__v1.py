class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        n = len(colors)
        mindist = [[-1] * n for _ in range(3)]
        for cc in range(3):
            c = cc + 1
            prev_pos = [-1] * n
            last = -1
            for i in range(n):
                if colors[i] == c:
                    prev_pos[i] = i
                    last = i
                else:
                    prev_pos[i] = last
            next_pos = [n] * n
            last = n
            for i in range(n - 1, -1, -1):
                if colors[i] == c:
                    next_pos[i] = i
                    last = i
                else:
                    next_pos[i] = last
            for i in range(n):
                cand_dist = n
                if prev_pos[i] != -1:
                    cand_dist = min(cand_dist, i - prev_pos[i])
                if next_pos[i] != n:
                    cand_dist = min(cand_dist, next_pos[i] - i)
                if cand_dist < n:
                    mindist[cc][i] = cand_dist
        return [mindist[q[1] - 1][q[0]] for q in queries]
