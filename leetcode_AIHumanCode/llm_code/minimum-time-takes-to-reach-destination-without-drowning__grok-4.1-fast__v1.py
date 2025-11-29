class Solution(object):
    def minimumSeconds(self, land):
        rows, cols = len(land), len(land[0])
        INF = 10**9 + 7
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fire_arrival = [[INF] * cols for _ in range(rows)]
        fire_front = []
        for x in range(rows):
            for y in range(cols):
                if land[x][y] == '*':
                    fire_arrival[x][y] = 0
                    fire_front.append((x, y))
        while fire_front:
            next_fire = []
            for x, y in fire_front:
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and land[nx][ny] != 'X' and land[nx][ny] != 'D' and fire_arrival[nx][ny] == INF:
                        fire_arrival[nx][ny] = fire_arrival[x][y] + 1
                        next_fire.append((nx, ny))
            fire_front = next_fire
        sx, sy = 0, 0
        for x in range(rows):
            for y in range(cols):
                if land[x][y] == 'S':
                    sx, sy = x, y
                    break
            else:
                continue
            break
        player_arrival = [[INF] * cols for _ in range(rows)]
        player_front = []
        if fire_arrival[sx][sy] > 0:
            player_arrival[sx][sy] = 0
            player_front.append((sx, sy))
        while player_front:
            next_player = []
            for x, y in player_front:
                if land[x][y] == 'D':
                    return player_arrival[x][y]
                t = player_arrival[x][y]
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and land[nx][ny] != 'X' and player_arrival[nx][ny] == INF and t + 1 < fire_arrival[nx][ny]:
                        player_arrival[nx][ny] = t + 1
                        next_player.append((nx, ny))
            player_front = next_player
        return -1
