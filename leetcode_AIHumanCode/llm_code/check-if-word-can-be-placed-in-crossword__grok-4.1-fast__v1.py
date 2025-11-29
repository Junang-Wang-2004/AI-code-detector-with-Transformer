class Solution:
    def placeWordInCrossword(self, board, word):
        rows, cols = len(board), len(board[0])
        rword = word[::-1]

        def fits(slot, pat):
            return len(slot) == len(pat) and all(slot[k] == ' ' or slot[k] == pat[k] for k in range(len(slot)))

        # Check rows
        for x in range(rows):
            gap = []
            for y in range(cols):
                cell = board[x][y]
                if cell == '#':
                    if fits(gap, word) or fits(gap, rword):
                        return True
                    gap = []
                else:
                    gap.append(cell)
            if fits(gap, word) or fits(gap, rword):
                return True

        # Check columns
        for y in range(cols):
            gap = []
            for x in range(rows):
                cell = board[x][y]
                if cell == '#':
                    if fits(gap, word) or fits(gap, rword):
                        return True
                    gap = []
                else:
                    gap.append(cell)
            if fits(gap, word) or fits(gap, rword):
                return True

        return False
