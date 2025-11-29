import collections

class Solution:
    def countPairs(self, nums):
        freq = collections.Counter(nums)
        ans = sum(v * (v - 1) // 2 for v in freq.values())
        for num, cnt_num in freq.items():
            s = f"{num:07d}"
            digits = [int(ch) for ch in s]
            for p in range(7):
                for q in range(p + 1, 7):
                    if digits[p] == digits[q]:
                        continue
                    temp_digits = digits[:]
                    temp_digits[p], temp_digits[q] = temp_digits[q], temp_digits[p]
                    partner = int(''.join(map(str, temp_digits)))
                    if partner > num:
                        ans += cnt_num * freq[partner]
        return ans
