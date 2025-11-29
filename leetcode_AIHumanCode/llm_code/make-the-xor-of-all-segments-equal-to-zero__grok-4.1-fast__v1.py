import collections

class Solution:
    def minChanges(self, nums, k):
        n = len(nums)
        group_freqs = [collections.Counter() for _ in range(k)]
        for i, val in enumerate(nums):
            group_freqs[i % k][val] += 1
        max_freq_list = [max(g.values() or [0]) for g in group_freqs]
        sac_keep = sum(max_freq_list) - min(max_freq_list)
        sac_chg = n - sac_keep
        xor_states = {0: 0}
        for freq_map in group_freqs:
            next_states = collections.defaultdict(int)
            for cur_xor, cur_keep in xor_states.items():
                for num, cnt in freq_map.items():
                    new_xor = cur_xor ^ num
                    next_states[new_xor] = max(next_states[new_xor], cur_keep + cnt)
            xor_states = next_states
        full_keep = xor_states.get(0, 0)
        full_chg = n - full_keep
        return min(sac_chg, full_chg)
