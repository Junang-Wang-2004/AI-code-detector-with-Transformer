# Time:  O(q + n * t)
# Space: O(t + n + q)

# radix sort
class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        """
        max_t = max(t for _, t in queries)
        lookup = [[] for _ in range(max_t+1)]
        for i, (k, t) in enumerate(queries):
            lookup[t].append((k, i))
        result = [0]*len(queries)
        idxs = list(range(len(nums)))
        for l in range(1, max_t+1):
            cnt = [0]*10
            for i in idxs:
                d = int(nums[i][-l])
                cnt[d] += 1
            for d in range(9):
                cnt[d+1] += cnt[d]
            new_idxs = [0]*len(nums)
            for i in reversed(idxs):
                d = int(nums[i][-l])
                cnt[d] -= 1
                new_idxs[cnt[d]] = i
            idxs = new_idxs
            for k, i in lookup[l]:
                result[i] = idxs[k-1]
        return result

            
