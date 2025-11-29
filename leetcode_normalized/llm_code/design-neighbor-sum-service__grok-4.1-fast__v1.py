class C1:

    def __init__(self, a1):
        self.board = a1
        v1 = len(a1)
        v2 = len(a1[0])
        self.side_sums = {}
        self.angle_sums = {}
        v3 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        v4 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for v5 in range(v1):
            for v6 in range(v2):
                v7 = self.board[v5][v6]
                v8 = 0
                for v9, v10 in v3:
                    v11 = v5 + v9
                    v12 = v6 + v10
                    if 0 <= v11 < v1 and 0 <= v12 < v2:
                        v8 += self.board[v11][v12]
                self.side_sums[v7] = v8
                v13 = 0
                for v9, v10 in v4:
                    v11 = v5 + v9
                    v12 = v6 + v10
                    if 0 <= v11 < v1 and 0 <= v12 < v2:
                        v13 += self.board[v11][v12]
                self.angle_sums[v7] = v13

    def adjacentSum(self, a1):
        return self.side_sums.get(a1, 0)

    def diagonalSum(self, a1):
        return self.angle_sums.get(a1, 0)
