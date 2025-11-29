class Solution(object):
    def maxLength(self, arr):
        def compute_mask(s):
            mask = 0
            for char in s:
                shift = ord(char) - ord('a')
                bit = 1 << shift
                if mask & bit:
                    return 0
                mask |= bit
            return mask

        masks = [compute_mask(s) for s in arr]

        def backtrack(idx, used, length):
            if idx == len(arr):
                return length
            res = backtrack(idx + 1, used, length)
            m = masks[idx]
            if m and (used & m) == 0:
                res = max(res, backtrack(idx + 1, used | m, length + len(arr[idx])))
            return res

        return backtrack(0, 0, 0)
