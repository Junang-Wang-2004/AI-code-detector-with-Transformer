class Solution:
    def numberOfSubmatrices(self, grid):
        count_x = 0
        count_y = 0
        total = 0
        for row in grid:
            for cell in row:
                if cell == 'X':
                    count_x += 1
                elif cell == 'Y':
                    count_y += 1
                if count_x == count_y and count_x != 0:
                    total += 1
        return total
