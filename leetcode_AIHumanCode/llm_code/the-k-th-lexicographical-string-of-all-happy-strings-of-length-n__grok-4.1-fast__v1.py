class Solution:
    def getHappyString(self, n, k):
        if n == 0:
            return ""
        res = []
        prev = None
        for pos in range(n):
            sz = 1 << (n - 1 - pos)
            found = False
            for ch in 'abc':
                if ch == prev:
                    continue
                if k <= sz:
                    res.append(ch)
                    prev = ch
                    found = True
                    break
                k -= sz
            if not found:
                return ""
        return ''.join(res)
