class Solution:
    def minDays(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def num_components():
            visited = [[False] * n for _ in range(m)]
            components = 0
            for x in range(m):
                for y in range(n):
                    if grid[x][y] and not visited[x][y]:
                        components += 1
                        stack = [(x, y)]
                        visited[x][y] = True
                        while stack:
                            cx, cy = stack.pop()
                            for dx, dy in delta:
                                nx, ny = cx + dx, cy + dy
                                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    stack.append((nx, ny))
            return components

        if num_components() != 1:
            return 0

        total_land = sum(sum(row) for row in grid)
        if total_land == 1:
            return 1

        def node(x, y):
            return x * n + y

        neighbors = [[] for _ in range(m * n)]
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    continue
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                        neighbors[node(x, y)].append(node(nx, ny))

        disc_time = [-1] * (m * n)
        lowest = [-1] * (m * n)
        par = [-1] * (m * n)
        is_ap = [False] * (m * n)
        timer = 0

        def explore(u):
            nonlocal timer
            child_cnt = 0
            disc_time[u] = lowest[u] = timer
            timer += 1
            for v in neighbors[u]:
                if disc_time[v] == -1:
                    par[v] = u
                    child_cnt += 1
                    explore(v)
                    lowest[u] = min(lowest[u], lowest[v])
                    if par[u] != -1 and lowest[v] >= disc_time[u]:
                        is_ap[u] = True
                    if par[u] == -1 and child_cnt > 1:
                        is_ap[u] = True
                elif v != par[u]:
                    lowest[u] = min(lowest[u], disc_time[v])

        start_node = next(node(x, y) for x in range(m) for y in range(n) if grid[x][y])
        explore(start_node)

        for flag in is_ap:
            if flag:
                return 1
        return 2
