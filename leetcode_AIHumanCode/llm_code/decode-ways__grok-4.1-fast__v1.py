class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        back2 = 1
        back1 = 1
        for pos in range(1, n):
            now = 0
            if s[pos] != '0':
                now = back1
            pair = s[pos - 1:pos + 1]
            if 10 <= int(pair) <= 26:
                now += back2
            back2 = back1
            back1 = now
        return back1
