class Solution(object):
    def subtreeInversionSum(self, edges, nums, k):
        n = len(nums)
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        accum = []
        def traverse(curr, prev):
            accum.append([0, 0])
            subt_sum = nums[curr]
            gain_a = 0
            gain_b = 0
            for next_node in graph[curr]:
                if next_node == prev:
                    continue
                ch_sum, ch_a, ch_b = traverse(next_node, curr)
                subt_sum += ch_sum
                gain_a += ch_a
                gain_b += ch_b
            gain_a = max(gain_a, accum[-1][1] - 2 * subt_sum)
            gain_b = max(gain_b, accum[-1][0] + 2 * subt_sum)
            accum.pop()
            path_len = len(accum)
            if path_len >= k:
                accum[path_len - k][0] += gain_a
                accum[path_len - k][1] += gain_b
            return subt_sum, gain_a, gain_b
        full_sum, final_gain, _ = traverse(0, -1)
        return full_sum + final_gain
