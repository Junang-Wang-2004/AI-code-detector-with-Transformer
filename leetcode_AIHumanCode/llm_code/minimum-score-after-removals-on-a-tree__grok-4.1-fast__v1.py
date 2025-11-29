class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        xor_all = 0
        for val in nums:
            xor_all ^= val
        min_score = 10**18
        def traverse(curr, par, xor_parts):
            acc_xor = nums[curr]
            for nxt in graph[curr]:
                if nxt != par:
                    sub_xor = traverse(nxt, curr, xor_parts)
                    acc_xor ^= sub_xor
            xor_parts.append(acc_xor)
            return acc_xor
        for src, dst in edges:
            part1 = []
            traverse(src, dst, part1)
            part2 = []
            traverse(dst, src, part2)
            for parts in (part1, part2):
                if not parts:
                    continue
                full_part = parts.pop()
                for sub_part in parts:
                    comp1 = xor_all ^ full_part
                    comp2 = sub_part
                    comp3 = full_part ^ sub_part
                    mx = max(comp1, comp2, comp3)
                    mn = min(comp1, comp2, comp3)
                    min_score = min(min_score, mx - mn)
        return min_score
