from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        cache = {}

        def get_chain(v: int) -> int:
            if v not in freq:
                return 0
            if v in cache:
                return cache[v]
            sq = v * v
            if freq[v] < 2 or sq not in freq:
                cache[v] = 1
            else:
                cache[v] = 2 + get_chain(sq)
            return cache[v]

        res = 0
        ones = freq[1]
        if ones > 0:
            res = ones if ones % 2 == 1 else ones - 1
        for key in freq:
            if key != 1:
                res = max(res, get_chain(key))
        return res
