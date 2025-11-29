class Solution(object):
    def isPossibleDivide(self, nums, k):
        freq = {}
        for val in nums:
            freq[val] = freq.get(val, 0) + 1
        for base in sorted(freq):
            rem = freq.get(base, 0)
            if rem <= 0:
                continue
            for j in range(k):
                pos = base + j
                if freq.get(pos, 0) < rem:
                    return False
                freq[pos] -= rem
        return True
