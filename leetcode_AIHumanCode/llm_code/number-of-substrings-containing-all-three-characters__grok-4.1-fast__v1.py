class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos_a = pos_b = pos_c = -1
        count = 0
        n = len(s)
        for i in range(n):
            if s[i] == 'a':
                pos_a = i
            elif s[i] == 'b':
                pos_b = i
            else:
                pos_c = i
            count += min(pos_a, pos_b, pos_c) + 1
        return count
