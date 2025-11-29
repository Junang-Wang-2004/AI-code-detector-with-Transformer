class Solution:
    def canDistribute(self, nums, quantity):
        freq_map = {}
        for val in nums:
            freq_map[val] = freq_map.get(val, 0) + 1
        supplies = sorted(freq_map.values(), reverse=True)
        m = len(quantity)
        full_mask = (1 << m) - 1
        subset_sums = [0] * (full_mask + 1)
        for mask in range(full_mask + 1):
            for i in range(m):
                if mask & (1 << i):
                    subset_sums[mask] += quantity[i]
        achievable = {0}
        for cap in supplies[:m]:
            new_set = set(achievable)
            for prev in achievable:
                rem = full_mask ^ prev
                submask = rem
                while submask:
                    if subset_sums[submask] <= cap:
                        new_set.add(prev | submask)
                    submask = (submask - 1) & rem
            achievable = new_set
        return full_mask in achievable
