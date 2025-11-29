class Solution:
    def longestSubsequence(self, s, k):
        seq = s[::-1]
        length = 0
        place = 1
        capacity = k
        for digit in seq:
            if digit == '0':
                length += 1
            elif place <= capacity:
                capacity -= place
                length += 1
            if place <= capacity:
                place *= 2
        return length
