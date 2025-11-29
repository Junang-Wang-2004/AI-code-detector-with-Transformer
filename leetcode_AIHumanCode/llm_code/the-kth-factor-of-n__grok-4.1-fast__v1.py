class Solution:
    def kthFactor(self, n, k):
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
            i += 1
        sz = len(divisors)
        sq = divisors and divisors[-1] * divisors[-1] == n
        pairs = sz - int(sq)
        tot = sz + pairs
        if k > tot:
            return -1
        if k <= sz:
            return divisors[k - 1]
        pos = k - sz
        idx = pairs - pos
        return n // divisors[idx]
