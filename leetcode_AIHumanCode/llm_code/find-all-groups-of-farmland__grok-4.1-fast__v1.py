class Solution:
    def findFarmland(self, land):
        if not land or not land[0]:
            return []
        height = len(land)
        width = len(land[0])
        farmland = []
        for row in range(height):
            for col in range(width):
                if land[row][col] == 0:
                    continue
                if row > 0 and land[row - 1][col] == 1:
                    continue
                if col > 0 and land[row][col - 1] == 1:
                    continue
                bot = row
                while bot + 1 < height and land[bot + 1][col] == 1:
                    bot += 1
                rite = col
                while rite + 1 < width and land[row][rite + 1] == 1:
                    rite += 1
                farmland.append([row, col, bot, rite])
        return farmland
