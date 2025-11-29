import collections

class Solution(object):
    def numTriplets(self, nums1, nums2):
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        def get_pairs(count, target):
            ans = 0
            for x in count:
                if target % x != 0:
                    continue
                y = target // x
                if y not in count:
                    continue
                if x < y:
                    ans += count[x] * count[y]
                elif x == y:
                    ans += count[x] * (count[x] - 1) // 2
            return ans
        res = 0
        for a in nums1:
            res += get_pairs(c2, a * a)
        for b in nums2:
            res += get_pairs(c1, b * b)
        return res
