class Solution(object):
    def removeDuplicates(self, s, k):
        buf = []
        for ch in s:
            buf.append(ch)
            while len(buf) >= k and buf[-k:] == [buf[-1]] * k:
                del buf[-k:]
        return ''.join(buf)
