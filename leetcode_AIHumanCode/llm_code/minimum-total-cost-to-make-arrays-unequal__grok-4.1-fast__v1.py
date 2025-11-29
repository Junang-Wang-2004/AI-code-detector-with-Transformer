import collections

class Solution(object):
    def minimumTotalCost(self, nums1, nums2):
        n = len(nums1)
        freq = collections.Counter()
        base_cost = 0
        match_count = 0
        for i in range(n):
            if nums1[i] == nums2[i]:
                val = nums1[i]
                freq[val] += 1
                base_cost += i
                match_count += 1
        if match_count == 0:
            return 0
        max_count = 0
        dom_val = None
        for v, c in freq.items():
            if c > max_count:
                max_count = c
                dom_val = v
        required = 2 * max_count - match_count
        if required <= 0:
            return base_cost
        candidates = []
        for i in range(n):
            x, y = nums1[i], nums2[i]
            if x != y and x != dom_val and y != dom_val:
                candidates.append(i)
        if len(candidates) < required:
            return -1
        candidates.sort()
        add_cost = sum(candidates[:required])
        return base_cost + add_cost
