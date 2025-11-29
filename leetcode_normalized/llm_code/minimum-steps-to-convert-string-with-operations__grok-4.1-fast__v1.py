class Solution(object):
    def minOperations(self, word1, word2):
        n = len(word1)
        dp_rev = [[0] * n for _ in range(n)]
        A = ord('a')
        for diag in range(2 * n - 1):
