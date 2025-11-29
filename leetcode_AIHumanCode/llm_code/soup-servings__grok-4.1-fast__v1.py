class Solution:
    def soupServings(self, N):
        if N >= 4800:
            return 1.0
        units = (N + 24) // 25
        table = [[0.0] * (units + 1) for _ in range(units + 1)]
        moves = [(4, 0), (3, 1), (2, 2), (1, 3)]
        for x in range(units + 1):
            for y in range(units + 1):
                if x == 0 and y == 0:
                    table[0][0] = 0.5
                elif x == 0:
                    table[0][y] = 1.0
                elif y == 0:
                    table[x][0] = 0.0
                else:
                    accum = 0.0
                    for dx, dy in moves:
                        nx = x - dx
                        ny = y - dy
                        if nx <= 0 and ny <= 0:
                            accum += 0.5
                        elif nx <= 0:
                            accum += 1.0
                        elif ny <= 0:
                            accum += 0.0
                        else:
                            accum += table[nx][ny]
                    table[x][y] = accum / 4
        return table[units][units]
