class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []
        for ln in range(1, 10):
            for st in range(1, 11 - ln):
                val = 0
                for k in range(ln):
                    val = val * 10 + st + k
                if low <= val <= high:
                    ans.append(val)
        return ans
