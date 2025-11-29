class Solution(object):
    def maximizeXorAndXor(self, nums):
        n = len(nums)
        N = 1 << n
        ALL_ONES = (1 << 32) - 1
        sub_and = [0] * N
        sub_xor = [0] * N
        sub_and[0] = ALL_ONES
        sub_xor[0] = 0
        for mask in range(1, N):
            idx = 0
            temp = mask
            while (temp & 1) == 0:
                idx += 1
                temp >>= 1
            prior = mask ^ (1 << idx)
            sub_and[mask] = sub_and[prior] & nums[idx]
            sub_xor[mask] = sub_xor[prior] ^ nums[idx]
        best = 0
        full_set = N - 1

        def highest_subset_xor(items):
            if not items:
                return 0
            bl = max(item.bit_length() for item in items)
            pivots = [0] * (bl + 1)
            for num in items:
                val = num
                for pos in range(bl, -1, -1):
                    if (val & (1 << pos)) == 0:
                        continue
                    if pivots[pos]:
                        val ^= pivots[pos]
                    else:
                        pivots[pos] = val
                        break
            outcome = 0
            for pos in range(bl, -1, -1):
                if pivots[pos] and (outcome ^ pivots[pos]) > outcome:
                    outcome ^= pivots[pos]
            return outcome

        for s in range(1, N):
            and_value = sub_and[s]
            comp_s = full_set ^ s
            xor_value = sub_xor[comp_s]
            masks = [nums[k] & ~xor_value for k in range(n) if (s & (1 << k)) == 0]
            bonus = highest_subset_xor(masks)
            total = and_value + xor_value + 2 * bonus
            if total > best:
                best = total
        return best
