class Solution:
    def tictactoe(self, moves):
        rowsA = [0] * 3
        colsA = [0] * 3
        diagA = 0
        antidiagA = 0
        rowsB = [0] * 3
        colsB = [0] * 3
        diagB = 0
        antidiagB = 0
        player = 'A'
        for x, y in moves:
            if player == 'A':
                rowsA[x] += 1
                colsA[y] += 1
                if x == y:
                    diagA += 1
                if x + y == 2:
                    antidiagA += 1
                if rowsA[x] == 3 or colsA[y] == 3 or diagA == 3 or antidiagA == 3:
                    return 'A'
            else:
                rowsB[x] += 1
                colsB[y] += 1
                if x == y:
                    diagB += 1
                if x + y == 2:
                    antidiagB += 1
                if rowsB[x] == 3 or colsB[y] == 3 or diagB == 3 or antidiagB == 3:
                    return 'B'
            player = 'B' if player == 'A' else 'A'
        return "Draw" if len(moves) == 9 else "Pending"
