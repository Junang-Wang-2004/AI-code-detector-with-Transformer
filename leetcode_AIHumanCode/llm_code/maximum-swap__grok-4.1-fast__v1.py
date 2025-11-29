class Solution(object):
    def maximumSwap(self, num):
        chars = list(str(num))
        n = len(chars)
        last_occurrence = [-1] * 10
        for i in range(n):
            d = int(chars[i])
            last_occurrence[d] = i
        for i in range(n):
            curr = int(chars[i])
            for candidate in range(9, curr, -1):
                j = last_occurrence[candidate]
                if j > i:
                    chars[i], chars[j] = chars[j], chars[i]
                    return int(''.join(chars))
        return int(''.join(chars))
