# Time:  O(n)
# Space: O(n)
import collections


# partial sort, freq table
class Solution2(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        """
        def check(cnt2, cnt1):
            # return cnt2 <= cnt1  # for python3
            return all(cnt1.get(k, 0)-v >= 0 for k, v in cnt2.items())  # for python2
        
        def topk(a, k):  # Time: O(k * n)
            result = [float("-inf")]*k
            for x in a:
                for i in range(len(result)):
                    if x > result[i]:
                        result[i], x = x, result[i]
            return result
    
        mx = max(nums2)
        cnt2 = collections.Counter(nums2)
        return next(d for d in [mx-x for x in topk(nums1, 3)] if check(cnt2, collections.Counter(x+d for x in nums1)))


