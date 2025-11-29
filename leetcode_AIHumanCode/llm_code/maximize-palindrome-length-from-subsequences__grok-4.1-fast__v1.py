class Solution:
    def longestPalindrome(self, word1, word2):
        text = word1 + word2
        total = len(text)
        split = len(word1)
        table = [[0] * total for _ in total]
        max_len = 0
        for pos in range(total):
            table[pos][pos] = 1
        for dist in range(2, total + 1):
            for left in range(total - dist + 1):
                right = left + dist - 1
                if text[left] == text[right]:
                    inside = 0 if dist == 2 else table[left + 1][right - 1]
                    table[left][right] = 2 + inside
                    if left < split <= right:
                        max_len = max(max_len, table[left][right])
                else:
                    table[left][right] = max(table[left + 1][right], table[left][right - 1])
        return max_len
