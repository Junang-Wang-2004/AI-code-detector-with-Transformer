# Time:  O(nlogk)
# Space: O(n)
class Solution3(object):
    def topKFrequent(self, nums, k):
        """
        """
        return [key for key, _ in collections.Counter(nums).most_common(k)]

