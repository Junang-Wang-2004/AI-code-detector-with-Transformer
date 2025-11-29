# Time:  O(k * C(n, k))
# Space: O(k)

class Solution(object):
    def combine(self, n, k):
        """
        """
        if k > n:
            return []
        nums, idxs = list(range(1, n+1)), list(range(k))
        result = [[nums[i] for i in idxs]]
        while True:
            for i in reversed(range(k)):
                if idxs[i] != i+n-k:
                    break
            else:
                break
            idxs[i] += 1
            for j in range(i+1, k):
                idxs[j] = idxs[j-1]+1
            result.append([nums[i] for i in idxs])
        return result


