import heapq

class Solution:
    def eatenApples(self, apples, days):
        pq = []
        score = 0
        turn = 0
        limit = len(apples)
        stock = apples[:]
        while turn < limit or pq:
            if turn < limit and stock[turn] > 0:
                heapq.heappush(pq, (turn + days[turn], turn))
            while pq and pq[0][0] <= turn:
                heapq.heappop(pq)
            if pq:
                _, pile = pq[0]
                stock[pile] -= 1
                if stock[pile] == 0:
                    heapq.heappop(pq)
                score += 1
            turn += 1
        return score
