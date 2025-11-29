class Solution:
    def pourWater(self, heights, V, K):
        n = len(heights)
        for _ in range(V):
            spot = K
            min_height = heights[K]
            j = K
            while j > 0 and heights[j - 1] <= min_height:
                j -= 1
                if heights[j] < min_height:
                    min_height = heights[j]
                    spot = j
            if spot != K:
                heights[spot] += 1
                continue
            min_height = heights[K]
            j = K
            spot = K
            while j + 1 < n and heights[j + 1] <= min_height:
                j += 1
                if heights[j] < min_height:
                    min_height = heights[j]
                    spot = j
            heights[spot] += 1
        return heights
