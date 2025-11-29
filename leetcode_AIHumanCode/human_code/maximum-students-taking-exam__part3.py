# Time:  O(|V| * |E|) = O(m^2 * n^2)
# Space: O(|V| + |E|) = O(m * n)
# Hungarian bipartite matching
class Solution2(object):
    def maxStudents(self, seats):
        """
        """
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
        def dfs(seats, e, lookup, matching):
            i, j = e
            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if 0 <= ni < len(seats) and 0 <= nj < len(seats[0]) and \
                    seats[ni][nj] == '.' and not lookup[ni][nj]:
                    lookup[ni][nj] = True
                    if matching[ni][nj] == -1 or dfs(seats, matching[ni][nj], lookup, matching):
                        matching[ni][nj] = e
                        return True
            return False
        
        def Hungarian(seats):
            result = 0
            matching = [[-1]*len(seats[0]) for _ in range(len(seats))]
            for i in range(len(seats)):
                for j in range(0, len(seats[0]), 2):
                    if seats[i][j] != '.':
                        continue
                    lookup = [[False]*len(seats[0]) for _ in range(len(seats))]
                    if dfs(seats, (i, j), lookup, matching):
                        result += 1
            return result
          
        count = 0
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == '.':
                    count += 1
        return count-Hungarian(seats)


