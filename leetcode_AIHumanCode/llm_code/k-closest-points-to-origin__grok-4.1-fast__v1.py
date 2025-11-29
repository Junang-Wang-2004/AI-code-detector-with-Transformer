import random

class Solution:
    def kClosest(self, points, K):
        random.shuffle(points)
        
        def squared_distance(p):
            return p[0] * p[0] + p[1] * p[1]
        
        def partition(low, high):
            pivot_dist = squared_distance(points[high])
            store = low
            for j in range(low, high):
                if squared_distance(points[j]) < pivot_dist:
                    points[store], points[j] = points[j], points[store]
                    store += 1
            points[store], points[high] = points[high], points[store]
            return store
        
        def select(start, end, target):
            if start >= end:
                return
            pos = partition(start, end)
            if pos == target:
                return
            elif pos > target:
                select(start, pos - 1, target)
            else:
                select(pos + 1, end, target)
        
        select(0, len(points) - 1, K - 1)
        return points[:K]
