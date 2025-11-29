class Solution:
    def partitionString(self, s):
        segments = 1
        active = set()
        for char in s:
            if char in active:
                segments += 1
                active.clear()
                active.add(char)
            else:
                active.add(char)
        return segments
