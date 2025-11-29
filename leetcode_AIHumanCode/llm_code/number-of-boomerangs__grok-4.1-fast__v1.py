class Solution:
    def numberOfBoomerangs(self, points):
        total = 0
        n = len(points)
        for i in range(n):
            dist_freq = {}
            for j in range(n):
                if i == j:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                distance = dx * dx + dy * dy
                dist_freq[distance] = dist_freq.get(distance, 0) + 1
            for freq in dist_freq.values():
                if freq > 1:
                    total += freq * (freq - 1)
        return total
