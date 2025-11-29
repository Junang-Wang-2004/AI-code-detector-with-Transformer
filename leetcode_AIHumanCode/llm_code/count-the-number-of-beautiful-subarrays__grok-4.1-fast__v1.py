class Solution:
    def beautifulSubarrays(self, nums):
        freq_map = {0: 1}
        answer = 0
        prefix_xor = 0
        for num in nums:
            prefix_xor ^= num
            answer += freq_map.get(prefix_xor, 0)
            freq_map[prefix_xor] = freq_map.get(prefix_xor, 0) + 1
        return answer
