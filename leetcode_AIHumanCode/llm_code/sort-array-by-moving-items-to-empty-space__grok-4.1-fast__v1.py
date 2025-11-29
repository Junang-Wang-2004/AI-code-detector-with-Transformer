class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        def get_cost(shift):
            vis = [False] * n
            cycles = 0
            long_cycles = 0
            for i in range(n):
                if vis[i]:
                    continue
                clen = 0
                cur = i
                while not vis[cur]:
                    vis[cur] = True
                    cur = (nums[cur] - shift) % n
                    clen += 1
                cycles += 1
                if clen >= 2:
                    long_cycles += 1
            total = n - cycles + 2 * long_cycles
            check_pos = (shift * (n - 1)) % n
            if nums[check_pos] != 0:
                total -= 2
            return total
        return min(get_cost(0), get_cost(1))
