from collections import defaultdict

class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        n = len(nums)
        answer = [0] * len(queries)
        max_len = max(trim for _, trim in queries)
        by_length = defaultdict(list)
        for qid, (rank, trim) in enumerate(queries):
            by_length[trim].append((rank, qid))
        order = list(range(n))
        for length in range(1, max_len + 1):
            buckets = [0] * 10
            for i in order:
                digit = int(nums[i][-(length)])
                buckets[digit] += 1
            for d in range(1, 10):
                buckets[d] += buckets[d - 1]
            fresh_order = [0] * n
            for i in reversed(order):
                digit = int(nums[i][-(length)])
                buckets[digit] -= 1
                fresh_order[buckets[digit]] = i
            order = fresh_order
            if length in by_length:
                for rank, qid in by_length[length]:
                    answer[qid] = order[rank - 1]
        return answer
