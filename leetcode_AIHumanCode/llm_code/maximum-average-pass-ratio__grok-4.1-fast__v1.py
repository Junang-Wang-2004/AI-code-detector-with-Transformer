import heapq

class Solution:
    def maxAverageRatio(self, teams, extraStudents):
        n = len(teams)
        squads = [list(mem) for mem in teams]
        def marg(p, tot):
            return (p + 1) / (tot + 1) - p / tot
        pq = []
        for i in range(n):
            p, tot = squads[i]
            heapq.heappush(pq, (-marg(p, tot), i))
        for _ in range(extraStudents):
            _, j = heapq.heappop(pq)
            p, tot = squads[j]
            squads[j][0] += 1
            squads[j][1] += 1
            heapq.heappush(pq, (-marg(p, tot), j))
        return sum(p / tot for p, tot in squads) / n
