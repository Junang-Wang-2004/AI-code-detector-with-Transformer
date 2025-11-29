class Solution(object):
    def resultArray(self, nums, k):
        counts = [0] * k
        suffix = {}
        for val in nums:
            r = val % k
            prefix = {r: 1}
            for s, amt in suffix.items():
                t = (s * r) % k
                prefix[t] = prefix.get(t, 0) + amt
            for m, q in prefix.items():
                counts[m] += q
            suffix = prefix
        return counts
