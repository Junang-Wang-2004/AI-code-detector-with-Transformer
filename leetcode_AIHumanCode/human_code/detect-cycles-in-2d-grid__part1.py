# Time:  O(m * n * α(n)) ~= O(m * n)
# Space: O(m * n)

class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))
        self.count = n

    def find_set(self, x):
       if self.set[x] != x:
           self.set[x] = self.find_set(self.set[x])  # path compression.
       return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = list(map(self.find_set, (x, y)))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1


class Solution(object):
    def containsCycle(self, grid):
        """
        """
        def index(n, i, j):
            return i*n + j
    
        union_find = UnionFind(len(grid)*len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i and j and grid[i][j] == grid[i-1][j] == grid[i][j-1] and \
                   union_find.find_set(index(len(grid[0]), i-1, j)) == \
                   union_find.find_set(index(len(grid[0]), i, j-1)):
                    return True
                if i and grid[i][j] == grid[i-1][j]:
                    union_find.union_set(index(len(grid[0]), i-1, j),
                                         index(len(grid[0]),i, j))
                if j and grid[i][j] == grid[i][j-1]:
                    union_find.union_set(index(len(grid[0]), i, j-1),
                                         index(len(grid[0]), i, j))
        return False


