class Solution:
    def kthCharacter(self, s, k):
        position = 0
        prefix = 0
        for ch in s:
            if ch == ' ':
                incr = 1
                position = 0
            else:
                position += 1
                incr = position
            prefix += incr
            if prefix >= k:
                return ch
