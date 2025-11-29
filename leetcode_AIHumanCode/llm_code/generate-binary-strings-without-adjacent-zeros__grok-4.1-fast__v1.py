class Solution:
    def validStrings(self, n):
        def build(pos, allow_zero):
            if pos == n:
                return [""]
            res = []
            if allow_zero:
                for tail in build(pos + 1, False):
                    res.append("0" + tail)
            for tail in build(pos + 1, True):
                res.append("1" + tail)
            return res
        return build(0, True)
