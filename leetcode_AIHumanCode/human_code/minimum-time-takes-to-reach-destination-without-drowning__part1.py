# Time:  O(m * n)
# Space: O(m * n)

# simulation, bfs
class Solution(object):
    def minimumSeconds(self, land):
        """
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        lookup = [[-1 if land[i][j] == "*" else 0 for j in range(len(land[0]))] for i in range(len(land))]
        q = [(i, j, -1) for i in range(len(land)) for j in range(len(land[0])) if land[i][j] == "*"]
        q.append(next((i, j, 1) for i in range(len(land)) for j in range(len(land[0])) if land[i][j] == "S"))
        lookup[q[-1][0]][q[-1][1]] = 1
        while q:
            new_q = []
            for i, j, d in q:
                if land[i][j] == "D":
                    return d-1
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < len(land) and 0 <= nj < len(land[0]) and land[ni][nj] != "X" and lookup[ni][nj] != -1):
                        continue
                    if d != -1 and lookup[ni][nj] == 0:
                        lookup[ni][nj] = 1
                        new_q.append((ni, nj, d+1))
                    elif d == -1 and land[ni][nj] != "D":
                        lookup[ni][nj] = -1
                        new_q.append((ni, nj, -1))
            q = new_q
        return -1


