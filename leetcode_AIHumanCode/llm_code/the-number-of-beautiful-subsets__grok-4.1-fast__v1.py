from collections import Counter

class Solution:
    def beautifulSubsets(self, nums, k):
        freq = Counter(nums)
        total = 1
        seen = set()
        for val in list(freq):
            if val - k in freq or val in seen:
                continue
            chain = []
            pos = val
            while pos in freq:
                chain.append(freq[pos])
                seen.add(pos)
                pos += k
            no_use = 1
            use = 0
            for c in chain:
                opts = (1 << c) - 1
                new_no = no_use + use
                new_use = no_use * opts
                no_use = new_no
                use = new_use
            total *= no_use + use
        return total - 1
