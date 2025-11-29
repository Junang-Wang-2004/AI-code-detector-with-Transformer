class Solution:
    def hasAllCodes(self, s, k):
        length = len(s)
        required = 1 << k
        if length < required:
            return False
        found = [False] * required
        val = 0
        for j in range(k):
            val = (val << 1) | int(s[j])
        found[val] = True
        msk = required - 1
        for idx in range(1, length - k + 1):
            val = ((val << 1) & msk) | int(s[idx + k - 1])
            found[val] = True
        return all(found)
