from collections import Counter

class Solution:
    def leastBricks(self, wall):
        seams = Counter()
        for row in wall:
            pos = 0
            for length in row[:-1]:
                pos += length
                seams[pos] += 1
        max_aligned = max(seams.values(), default=0)
        return len(wall) - max_aligned
