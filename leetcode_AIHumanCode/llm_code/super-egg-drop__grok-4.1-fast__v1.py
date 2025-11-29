class Solution(object):
    def superEggDrop(self, K, N):
        floors = [0] * (K + 1)
        drops = 0
        while floors[K] < N:
            drops += 1
            for eggs in range(K, 0, -1):
                floors[eggs] += floors[eggs - 1] + 1
        return drops
