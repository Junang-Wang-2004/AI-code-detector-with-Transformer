class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def count_bits(x: int) -> int:
            return bin(x).count('1')

        n = len(s)
        prefix_restarts = [0] * (n + 1)
        prefix_last_mask = [0] * (n + 1)
        cur_mask = 0
        restarts = 0
        for idx in range(n):
            char_bit = 1 << (ord(s[idx]) - ord('a'))
            tentative_mask = cur_mask | char_bit
            if count_bits(tentative_mask) > k:
                restarts += 1
                cur_mask = char_bit
            else:
                cur_mask = tentative_mask
            prefix_restarts[idx + 1] = restarts
            prefix_last_mask[idx + 1] = cur_mask

        suffix_restarts = [0] * (n + 1)
        suffix_first_mask = [0] * (n + 1)
        cur_mask = 0
        restarts = 0
        for idx in range(n - 1, -1, -1):
            char_bit = 1 << (ord(s[idx]) - ord('a'))
            tentative_mask = cur_mask | char_bit
            if count_bits(tentative_mask) > k:
                restarts += 1
                cur_mask = char_bit
            else:
                cur_mask = tentative_mask
            suffix_restarts[idx] = restarts
            suffix_first_mask[idx] = cur_mask

        max_parts = 0
        for pos in range(n):
            base = prefix_restarts[pos] + suffix_restarts[pos + 1]
            combined_mask = prefix_last_mask[pos] | suffix_first_mask[pos + 1]
            left_unique = count_bits(prefix_last_mask[pos])
            right_unique = count_bits(suffix_first_mask[pos + 1])
            union_unique = count_bits(combined_mask)
            extra = 1
            if left_unique == k == right_unique and union_unique != 26:
                extra = 3
            elif union_unique + (union_unique != 26) > k:
                extra = 2
            max_parts = max(max_parts, base + extra)
        return max_parts
