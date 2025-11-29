# Time:  O(n + tlogt), t = threshold
# Space: O(t)
# union find, number theory
class Solution2(object):
    def countComponents(self, nums, threshold):
        """
        """
        uf = UnionFind(threshold)
        lookup = [-1]*threshold
        for x in nums:
            if x-1 >= threshold:
                continue
            for i in range(x+x, threshold+1, x):
                uf.union_set(i-1, x-1)
        return sum(x-1 >= threshold or uf.find_set(x-1) == x-1 for x in nums)
