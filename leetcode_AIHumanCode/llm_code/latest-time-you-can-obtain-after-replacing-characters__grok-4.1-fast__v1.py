class Solution:
    def findLatestTime(self, s):
        t = list(s)
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        a, b = t[0], t[1]
        if a == '?' and b == '?':
            t[0], t[1] = '2', '3'
        elif a == '?':
            t[0] = '2' if b <= '3' else '1'
        elif b == '?':
            t[1] = '3' if a == '2' else '9'
        return ''.join(t)
