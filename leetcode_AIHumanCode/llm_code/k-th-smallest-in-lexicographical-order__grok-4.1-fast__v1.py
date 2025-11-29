class Solution:
    def findKthNumber(self, n, k):
        def count(p):
            res = 0
            pw = 1
            while p * pw <= n:
                res += pw
                pw *= 10
            level_size = pw // 10
            if level_size > 0:
                start = p * level_size
                end = min(n, (p + 1) * level_size - 1)
                actual = max(0, end - start + 1)
                res += actual - level_size
            return res

        prefix = 0
        rem_k = k
        while True:
            start_d = 1 if prefix == 0 else 0
            for d in range(start_d, 10):
                next_prefix = prefix * 10 + d
                if next_prefix > n:
                    continue
                cnt = count(next_prefix)
                if rem_k <= cnt:
                    prefix = next_prefix
                    if rem_k == 1:
                        return prefix
                    rem_k -= 1
                    break
                rem_k -= cnt
