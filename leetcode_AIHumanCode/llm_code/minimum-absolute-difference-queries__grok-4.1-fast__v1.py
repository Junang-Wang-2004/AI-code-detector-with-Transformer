class Solution:
    def minDifference(self, nums, queries):
        n = len(nums)
        if n == 0:
            return []
        max_val = max(nums)
        block_size = int(n ** 0.5) + 1
        qlist = [(l // block_size, r, i, l, r) for i, (l, r) in enumerate(queries)]
        qlist.sort()
        result = [0] * len(queries)
        counts = [0] * (max_val + 1)
        left = 0
        right = -1

        def insert(idx):
            counts[nums[idx]] += 1

        def delete(idx):
            counts[nums[idx]] -= 1

        for _, r_end, qid, q_left, q_right in qlist:
            while right < q_right:
                right += 1
                insert(right)
            while left > q_left:
                left -= 1
                insert(left)
            while right > q_right:
                delete(right)
                right -= 1
            while left < q_left:
                delete(left)
                left += 1
            gap = float('inf')
            prev_val = -1
            for val in range(max_val + 1):
                if counts[val] > 0:
                    if prev_val != -1:
                        gap = min(gap, val - prev_val)
                    prev_val = val
            result[qid] = gap if gap != float('inf') else -1
        return result
