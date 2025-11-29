class Solution(object):
    def countGoodIntegers(self, n, k):
        facts = [1]
        for i in range(1, n + 1):
            facts.append(facts[-1] * i)
        length = (n + 1) // 2
        start = 10 ** (length - 1)
        end = 10 ** length
        freqs = set()
        total = 0
        for prefix in range(start, end):
            s = str(prefix)
            if n % 2:
                pal_s = s[:-1] + s[::-1]
            else:
                pal_s = s + s[::-1]
            num = int(pal_s)
            if num % k:
                continue
            counts = [0] * 10
            for ch in pal_s:
                counts[int(ch)] += 1
            t = tuple(counts)
            if t in freqs:
                continue
            freqs.add(t)
            den = 1
            for c in counts:
                den *= facts[c]
            ways = (n - counts[0]) * facts[n - 1] // den
            total += ways
        return total
