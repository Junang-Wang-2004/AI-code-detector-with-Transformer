class Solution(object):
    def minInsertions(self, s):
        n = len(s)
        insertions = [[0] * n for _ in range(n)]
        for start in range(n - 1):
            insertions[start][start + 1] = 0 if s[start] == s[start + 1] else 1
        for size in range(3, n + 1):
            for left in range(n - size + 1):
                right = left + size - 1
                if s[left] == s[right]:
                    insertions[left][right] = insertions[left + 1][right - 1]
                else:
                    insertions[left][right] = 1 + min(insertions[left][right - 1], insertions[left + 1][right])
        return insertions[0][n - 1]
