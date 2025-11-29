class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        memo = {}

        def helper(idx1, idx2, size):
            key = (idx1, idx2, size)
            if key in memo:
                return memo[key]
            if size == 1:
                res = s1[idx1] == s2[idx2]
            else:
                if s1[idx1:idx1 + size] == s2[idx2:idx2 + size]:
                    res = True
                else:
                    res = False
                    for split in range(1, size):
                        if (helper(idx1, idx2, split) and helper(idx1 + split, idx2 + split, size - split)) or \
                           (helper(idx1, idx2 + size - split, split) and helper(idx1 + split, idx2, size - split)):
                            res = True
                            break
            memo[key] = res
            return res

        return helper(0, 0, len(s1))
