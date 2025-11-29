from collections import defaultdict
from typing import List

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        total_subs = n * (n + 1) // 2

        # Compute sum of distinct over all subarrays
        sum_distinct = 0
        last_pos = {}
        prev_pos = [-1] * n
        for i in range(n):
            val = nums[i]
            prev_pos[i] = last_pos.get(val, -1)
            left_span = i - prev_pos[i]
            sum_distinct += left_span * (n - i)
            last_pos[val] = i

        # Positions per value
        positions = defaultdict(list)
        for i in range(n):
            positions[nums[i]].append(i)

        # Compute sum of edges (consecutive pairs both present)
        sum_edges = 0
        vals_set = set(positions.keys())
        def gaps_subs(plist: List[int], nn: int) -> int:
            if not plist:
                return total_subs
            res = 0
            prv = -1
            for p in plist:
                sz = p - prv - 1
                res += sz * (sz + 1) // 2
                prv = p
            sz = nn - prv - 1
            res += sz * (sz + 1) // 2
            return res

        def merge_lists(a: List[int], b: List[int]) -> List[int]:
            res = []
            i, j = 0, 0
            la, lb = len(a), len(b)
            while i < la and j < lb:
                if a[i] < b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            res.extend(a[i:])
            res.extend(b[j:])
            return res

        for v in list(vals_set):
            nv = v + 1
            if nv in vals_set:
                a_pos = positions[v]
                b_pos = positions[nv]
                avoid_a = gaps_subs(a_pos, n)
                avoid_b = gaps_subs(b_pos, n)
                union_pos = merge_lists(a_pos, b_pos)
                avoid_union = gaps_subs(union_pos, n)
                both = total_subs - avoid_a - avoid_b + avoid_union
                sum_edges += both

        return sum_distinct - sum_edges
