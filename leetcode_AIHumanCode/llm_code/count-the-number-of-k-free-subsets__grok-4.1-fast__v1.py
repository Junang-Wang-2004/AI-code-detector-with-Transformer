import collections

class Solution(object):
    def countTheNumOfKFreeSubsets(self, nums, k):
        freq = collections.Counter(nums)
        presents = set(freq)
        sorted_keys = sorted(freq)
        answer = 1
        for num in sorted_keys:
            if num - k in presents:
                continue
            prev_free = 1
            prev_taken = 0
            current = num
            while current in freq:
                multiplicity = freq[current]
                non_empty_opts = (2 ** multiplicity) - 1
                next_free = prev_free + prev_taken
                next_taken = prev_free * non_empty_opts
                prev_free = next_free
                prev_taken = next_taken
                current += k
            total_for_chain = prev_free + prev_taken
            answer *= total_for_chain
        return answer
