class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        n = len(s)
        maximum = 0
        idx = 0
        prior_length = 0
        prior_char = -1
        while idx < n:
            begin = idx
            while idx < n and s[idx] == s[begin]:
                idx += 1
            current_length = idx - begin
            current_char = int(s[begin])
            if prior_char == 0 and current_char == 1:
                maximum = max(maximum, 2 * min(prior_length, current_length))
            prior_length = current_length
            prior_char = current_char
        return maximum
