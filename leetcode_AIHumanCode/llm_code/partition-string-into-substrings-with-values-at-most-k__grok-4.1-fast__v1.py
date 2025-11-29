class Solution(object):
    def minimumPartition(self, s, k):
        n = len(s)
        pos = 0
        parts = 0
        while pos < n:
            end = pos
            val = 0
            while end < n:
                temp = val * 10 + int(s[end])
                if temp > k:
                    break
                val = temp
                end += 1
            if end == pos:
                return -1
            parts += 1
            pos = end
        return parts
