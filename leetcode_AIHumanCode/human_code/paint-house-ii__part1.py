from functools import reduce
# Time:  O(n * k)
# Space: O(k)

class Solution2(object):
    def minCostII(self, costs):
        """
        """
        return min(reduce(self.combine, costs)) if costs else 0

    def combine(self, tmp, house):
        smallest, k, i = min(tmp), len(tmp), tmp.index(min(tmp))
        tmp, tmp[i] = [smallest] * k, min(tmp[:i] + tmp[i+1:])
        return list(map(sum, list(zip(tmp, house))))


