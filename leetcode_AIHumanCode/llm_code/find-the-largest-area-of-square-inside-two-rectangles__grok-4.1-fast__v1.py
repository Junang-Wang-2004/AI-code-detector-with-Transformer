class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def overlap_side(bl1, tr1, bl2, tr2):
            left = max(bl1[0], bl2[0])
            right = min(tr1[0], tr2[0])
            bot = max(bl1[1], bl2[1])
            tp = min(tr1[1], tr2[1])
            wd = max(0, right - left)
            ht = max(0, tp - bot)
            return min(wd, ht)
        
        n = len(bottomLeft)
        max_side = 0
        for i in range(n):
            for j in range(i + 1, n):
                side = overlap_side(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])
                if side > max_side:
                    max_side = side
        return max_side * max_side
