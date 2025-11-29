class Solution:
    def partition(self, s):
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_pal[i][i + 1] = True
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True
        
        memo = [None] * (n + 1)
        
        def find_partitions(pos):
            if pos == n:
                return [[]]
            if memo[pos] is not None:
                return memo[pos]
            partitions = []
            for end in range(pos, n):
                if is_pal[pos][end]:
                    suffixes = find_partitions(end + 1)
                    for suffix in suffixes:
                        partitions.append([s[pos:end + 1]] + suffix)
            memo[pos] = partitions
            return partitions
        
        return find_partitions(0)
