# Time:  O(q + nlogn * t)
# Space: O(t + n + q)
# sort
class Solution3(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        """
        def compare(a, b):
            for i in range(len(nums[a])-t, len(nums[a])):
                if nums[a][i] < nums[b][i]:
                    return -1
                if nums[a][i] > nums[b][i]:
                    return 1
            return cmp(a, b)

        max_t = max(t for _, t in queries)
        lookup = [[] for _ in range(max_t+1)]
        for i, (k, t) in enumerate(queries):
            lookup[t].append((k, i))
        result = [0]*len(queries)
        idxs = list(range(len(nums)))
        for t in range(1, max_t+1):
            if not lookup[t]:
                continue
            idxs.sort(cmp=compare)
            for k, i in lookup[t]:
                result[i] = idxs[k-1]
        return result
