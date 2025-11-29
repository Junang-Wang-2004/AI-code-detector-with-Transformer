class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        if k == 0:
            return [0] * n
        sz = abs(k)
        offset = 1 if k > 0 else k
        extended = code + code
        prefix = [0] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            prefix[i] = prefix[i - 1] + extended[i - 1]
        result = [0] * n
        for i in range(n):
            start = (i + offset) % n
            if start + sz <= n:
                result[i] = prefix[start + sz] - prefix[start]
            else:
                result[i] = prefix[n] - prefix[start] + prefix[start + sz - n]
        return result
