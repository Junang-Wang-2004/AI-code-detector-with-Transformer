class Solution:
    def queryResults(self, limit, queries):
        mapping = {}
        freqs = {}
        output = [0] * len(queries)
        for pos, (key, val) in enumerate(queries):
            if key in mapping:
                prior = mapping[key]
                freqs[prior] -= 1
                if freqs[prior] == 0:
                    del freqs[prior]
            mapping[key] = val
            if val not in freqs:
                freqs[val] = 0
            freqs[val] += 1
            output[pos] = len(freqs)
        return output
