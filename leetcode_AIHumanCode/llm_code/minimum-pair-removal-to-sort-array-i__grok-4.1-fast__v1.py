import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        prev_node = [-1] * n
        for i in range(1, n):
            prev_node[i] = i - 1
        next_node = [i + 1 for i in range(n - 1)] + [-1]
        is_live = [True] * n
        num_bad = sum(nums[i] > nums[i + 1] for i in range(n - 1))
        pair_version = [0] * n
        min_heap = []
        for i in range(n - 1):
            heapq.heappush(min_heap, (nums[i] + nums[i + 1], pair_version[i], i))
        steps = 0
        while num_bad > 0:
            while min_heap:
                total, ver, begin = heapq.heappop(min_heap)
                following = next_node[begin]
                if (following == -1 or not is_live[begin] or not is_live[following] or
                    prev_node[following] != begin or ver != pair_version[begin]):
                    continue
                prior = prev_node[begin]
                has_prior = prior != -1 and is_live[prior]
                after = next_node[following]
                has_after = after != -1 and is_live[after]
                if has_prior and nums[prior] > nums[begin]:
                    num_bad -= 1
                if nums[begin] > nums[following]:
                    num_bad -= 1
                if has_after and nums[following] > nums[after]:
                    num_bad -= 1
                nums[begin] += nums[following]
                next_node[begin] = after
                if has_after:
                    prev_node[after] = begin
                is_live[following] = False
                if has_prior and nums[prior] > nums[begin]:
                    num_bad += 1
                if has_after and nums[begin] > nums[after]:
                    num_bad += 1
                if has_prior:
                    pair_version[prior] += 1
                    heapq.heappush(min_heap, (nums[prior] + nums[begin], pair_version[prior], prior))
                if has_after:
                    pair_version[begin] += 1
                    heapq.heappush(min_heap, (nums[begin] + nums[after], pair_version[begin], begin))
                steps += 1
                break
            else:
                break
        return steps
