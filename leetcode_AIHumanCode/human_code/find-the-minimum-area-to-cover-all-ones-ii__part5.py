        # Time:  ctor:  O(NlogN) * O(fn)
        #        query: O(fn)
        # Space: O(NlogN)
        class SparseTable(object):
            def __init__(self, arr, fn):
                self.fn = fn
                self.bit_length = [0]
                n = len(arr)
                k = n.bit_length()-1  # log2_floor(n)
                for i in range(k+1):
                    self.bit_length.extend(i+1 for _ in range(min(1<<i, (n+1)-len(self.bit_length))))
                self.st = [[0]*n for _ in range(k+1)]
                self.st[0] = arr[:]
                for i in range(1, k+1):  # Time: O(NlogN) * O(fn)
                    for j in range((n-(1<<i))+1):
                        self.st[i][j] = fn(self.st[i-1][j], self.st[i-1][j+(1<<(i-1))])
        
            def query(self, L, R):  # Time: O(fn)
                i = self.bit_length[R-L+1]-1  # log2_floor(R-L+1)
                return self.fn(self.st[i][L], self.st[i][R-(1<<i)+1])

        def minimumArea(min_i, max_i, min_j, max_j):
            min_r = min(st_min_i[min_i].query(min_j, max_j), max_i+1)
            max_r = max(st_max_i[max_i].query(min_j, max_j), min_i-1)
            min_c = min(st_min_j[min_j].query(min_i, max_i), max_j+1)
            max_c = max(st_max_j[max_j].query(min_i, max_i), min_j-1)
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0

        result = float("inf")
        for _ in range(4):
            st_min_i = [None]*len(grid)
            curr = [len(grid)]*len(grid[0])
            for i in reversed(range(len(grid))):
                for j in range(len(grid[0])):
                    if grid[i][j]:
                        curr[j] = i
                st_min_i[i] = SparseTable(curr, min)
            st_max_i = [None]*len(grid)
            curr = [-1]*len(grid[0])
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]:
                        curr[j] = i
                st_max_i[i] = SparseTable(curr, max)
            st_min_j = [None]*len(grid[0])
            curr = [len(grid[0])]*len(grid)
            for j in reversed(range(len(grid[0]))):
                for i in range(len(grid)):
                    if grid[i][j]:
                        curr[i] = j
                st_min_j[j] = SparseTable(curr, min)
            st_max_j = [None]*len(grid[0])
            curr = [-1]*len(grid)
            for j in range(len(grid[0])):
                for i in range(len(grid)):
                    if grid[i][j]:
                        curr[i] = j
                st_max_j[j] = SparseTable(curr, max)        
            for i in range(len(grid)-1):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(len(grid[0])-1):
                    b = minimumArea(i+1, len(grid)-1, 0, j)
                    c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                    result = min(result, a+b+c)
            for i in range(len(grid)-2):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(i+1, len(grid)-1):
                    b = minimumArea(i+1, j, 0, len(grid[0])-1)
                    c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                    result = min(result, a+b+c)
            grid = list(zip(*grid[::-1]))
        return result


