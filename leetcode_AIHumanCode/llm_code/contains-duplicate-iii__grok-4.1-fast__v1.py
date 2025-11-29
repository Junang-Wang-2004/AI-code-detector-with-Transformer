from collections import deque

class Solution(object):
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        buck_map = {}
        q = deque()
        def bucketize(val):
            return val if t == 0 else val // t
        for idx, val in enumerate(nums):
            while q and q[0] < idx - k:
                old_idx = q.popleft()
                old_buck = bucketize(nums[old_idx])
                if old_buck in buck_map and buck_map[old_buck] == old_idx:
                    del buck_map[old_buck]
            curr_buck = bucketize(val)
            for off in (-1, 0, 1):
                neigh_buck = curr_buck + off
                if neigh_buck in buck_map:
                    prev_idx = buck_map[neigh_buck]
                    if abs(val - nums[prev_idx]) <= t:
                        return True
            buck_map[curr_buck] = idx
            q.append(idx)
        return False
