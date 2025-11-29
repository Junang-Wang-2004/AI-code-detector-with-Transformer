class Solution(object):
    def countAsterisks(self, s):
        segments = s.split('|')
        return sum(seg.count('*') for seg in segments[::2])
