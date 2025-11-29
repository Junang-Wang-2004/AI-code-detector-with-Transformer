class Solution:
    def smallestPalindrome(self, s, k):
        n = len(s)
        h = n // 2
        f = [0] * 26
        for ch in s[:h]:
            f[ord(ch) - 97] += 1
        t = 0
        w = 1
        b = -1
        r = 0
        for ci in range(25, -1, -1):
            for u in range(1, f[ci] + 1):
                t += 1
                w = w * t // u
                if w >= k:
                    b = ci
                    r = f[ci] - u
                    break
            if b != -1:
                break
        if b == -1:
            return ""
        res = []
        for j in range(b + 1):
            num = r if j == b else f[j]
            chh = chr(97 + j)
            res += [chh] * num
            f[j] -= num
        while t > 0:
            for j in range(b, 26):
                if f[j] == 0:
                    continue
                nw = w * f[j] // t
                if nw < k:
                    k -= nw
                    continue
                w = nw
                f[j] -= 1
                t -= 1
                res.append(chr(97 + j))
                break
        if n % 2:
            res.append(s[h])
        return "".join(res + res[:h][::-1])
