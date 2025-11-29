class Solution:
    def concatenatedDivisibility(self, nums, k):
        if not nums:
            return []
        n = len(nums)
        digits_count = [len(str(x)) for x in nums]
        max_digits = max(digits_count)
        powers_of_ten = [1 % k]
        for _ in range(max_digits):
            powers_of_ten.append((powers_of_ten[-1] * 10) % k)
        total_mask = (1 << n) - 1
        reachable = [[False] * k for _ in range(1 << n)]
        reachable[total_mask][0] = True
        for bits in range(total_mask - 1, -1, -1):
            for mod in range(k):
                for pos in range(n):
                    if bits & (1 << pos):
                        continue
                    dig_len = digits_count[pos]
                    multiplier = powers_of_ten[dig_len]
                    new_mod = (mod * multiplier + nums[pos]) % k
                    new_bits = bits | (1 << pos)
                    if reachable[new_bits][new_mod]:
                        reachable[bits][mod] = True
                        break
        if not reachable[0][0]:
            return []
        prefs = sorted((nums[j], j) for j in range(n))
        path = []
        active_bits = 0
        active_mod = 0
        for _ in range(n):
            for _, pos in prefs:
                if active_bits & (1 << pos):
                    continue
                dig_len = digits_count[pos]
                multiplier = powers_of_ten[dig_len]
                new_mod = (active_mod * multiplier + nums[pos]) % k
                new_bits = active_bits | (1 << pos)
                if reachable[new_bits][new_mod]:
                    path.append(nums[pos])
                    active_bits = new_bits
                    active_mod = new_mod
                    break
        return path
